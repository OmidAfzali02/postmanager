from django.forms import ModelForm
from .models import User, Package, Agent, Address

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = '__all__'

class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'