from neuron.registry import registry
from .accounts.services import LoginService

# Account Services
registry.register(name='login', service=LoginService)