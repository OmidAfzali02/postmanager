from django.urls import path
from .views import *

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('register/', userRegister, name='register'),
    path('logout/', userLogout, name='logout'),

    path('profile/<int:pk>/', userProfile, name='logout'),

    path('send/', send_package, name='send'),
    # path('track/', login, name='track'),

    path('address/<int:pk>', edit_address, name='edit_address'),
    path('address/create', createAddress, name='create_address'),
    path('address/delete/<int:pk>', deleteAddress, name='delete_address'),

    path('agent/signup/', agentSetup, name='agent_signup'),
    path('agent/login/<int:pk>/', agentProfile, name='agent_profile'),
    
]