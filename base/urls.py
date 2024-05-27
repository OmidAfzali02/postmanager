from django.urls import path
from .views import *

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    # path('signup/', login, name='signup'),
    # path('send/', login, name='send'),
    # path('track/', login, name='track'),
    # path('agent_signup/', login, name='agent_signup'),
    
]