from django.contrib import admin
from .models import User, Agent, Package, Address

# Register your models here.
admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Package)
admin.site.register(Address)