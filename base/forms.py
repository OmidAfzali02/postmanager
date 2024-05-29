from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Package, Agent, Address

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')



class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = '__all__'
        exclude = ('location', 'sender_agency', 'receiver_agency', 'qr_code', )

class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'