from django.urls import path
from django.urls.resolvers import URLPattern

from .views import *

urlpatterns = [
    path('', HistoryListView.as_view(), name='history'),
    path('delete/<int:pk>', HistoryDelete.as_view(), name='history_delete')
]