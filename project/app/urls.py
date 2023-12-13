from django.urls import path
from .views import *

urlpatterns = [
    path('', autorize, name='autorize'),
    path('registration/', registration, name='registration'),
    path('successAutorize/', successAutorize, name='successAutorize'),
    path('successRegistration/', successRegistration, name='successRegistration')
]