from django.contrib import admin
from .models import User, Agent, package

# Register your models here.
admin.site.register(User)
admin.site.register(Agent)
admin.site.register(package)