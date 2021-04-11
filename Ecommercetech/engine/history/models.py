from django.db import models
from django.db.models.base import Model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .signal import object_viewed_signal
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class History(models.Model):
    # user = models.get_user_model()
    user           = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type   = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)  #product, blog
    object_id      = models.PositiveBigIntegerField()  #1,2,3,
    content_object = GenericForeignKey()
    visited_on     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content_object} visited: {self.visited_on}"
    
    class Meta:
        verbose_name_plural = "Histories"


def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    new_history = History.objects.create(
        user = request.user,
        content_type = ContentType.objects.get_for_model(sender),
        object_id = instance.id
    )

object_viewed_signal.connect(object_viewed_receiver)