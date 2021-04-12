from Ecommercetech.engine.accounts.serializers import LoginSerializer
from neuron.service import BaseService


class LoginService(BaseService):
    is_global = True
    
    def run(self, *args, **kwargs):
        data = self.request.data
        user_dict = data.get('user_dict')

        serializer = LoginSerializer(data=user_dict)
        serializer.is_valid(raise_exception=True)
        return serializer.data
