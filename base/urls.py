from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('register/', userRegister, name='register'),
    path('logout/', userLogout, name='logout'),

    path('profile/<int:pk>/', userProfile, name='profile'),

    path('send/', send_package, name='send'),
    path('track/<str:pk>/', track_package, name='track'),
    path('package/transfer/', package_change_status, name='package_change_status'),

    path('address/<int:pk>', edit_address, name='edit_address'),
    path('address/create', createAddress, name='create_address'),
    path('address/delete/<int:pk>', deleteAddress, name='delete_address'),

    path('agent/signup/', agentSetup, name='agent_signup'),
    path('agent/login/', agentLogin, name='agent_login'),
    path('agent/<int:pk>', agentProfile, name='agent_profile'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)