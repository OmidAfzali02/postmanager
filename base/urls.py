from django.urls import path
from .views import *

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('register/', userRegister, name='register'),
    path('logout/', userLogout, name='logout'),
    path('send/', send_package, name='send'),
    # path('track/', login, name='track'),
    # path('agent_signup/', login, name='agent_signup'),
    
]