from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

import uuid

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

gender_choices = (('male', 'male'), ('female', 'female'))

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=10)
    birth_date = models.DateField(blank=True, null=True, editable=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='image/avatar')
    gender = models.CharField(blank=True, null=True, max_length=20, choices=gender_choices)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Address(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    province = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    address = models.TextField(default=str)
    postal_code = models.CharField(max_length=10, default=str, unique=True)

    def __str__(self):
        return str(self.id) + ', ' + str(self.customer)
    

class Agent(models.Model):
    agent = models.OneToOneField(User, on_delete=models.CASCADE)
    agency_address = models.TextField()
    agency_postal_code = models.CharField(max_length=10)
    agency_phone = models.CharField(max_length=10)
    agency_province = models.CharField(max_length=20)
    agency_city = models.CharField(max_length=30)
    open_time = models.CharField(max_length=50, blank=True, default=str)

    def __str__(self):
        return str(self.id) + ', ' + str(self.agent.name)

delivery_choices = (('At agency', 'At agency'), ('At customer home', 'At customer home'))

class Package(models.Model):
    id = models.UUIDField(primary_key=True ,verbose_name='package id', default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    qr_code = models.ImageField(blank=True, null=True, upload_to='media/packages')
    contents = models.CharField(max_length=100, blank=True, default=str)
    length = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name="Package length in cm")
    width = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name="Package width in cm")
    height = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name="Package height in cm")
    weight = models.PositiveSmallIntegerField(default=0, verbose_name="Package weight in grams")
    location = models.JSONField(blank=True, default=list)
    delivery = models.CharField(max_length=30, choices=delivery_choices)

    sender_name = models.CharField(max_length=20)
    sender_phone = models.CharField(max_length=10)
    sender_address = models.TextField()
    sender_postal_code = models.CharField(max_length=10, blank=True, default=str)
    sender_agency = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='Sended_agency', blank=True, null=True)

    receiver_name = models.CharField(max_length=20)
    receiver_phone = models.CharField(max_length=10)
    receiver_address = models.TextField()
    receiver_postal_code = models.CharField(max_length=10, blank=True, default=str)
    receiver_agency = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='Received_agency', blank=True, null=True)

    def __str__(self):
        return str(self.sender_agency) +' to '+ str(self.receiver_agency) + ', ' + str(self.id)