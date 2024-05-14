from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

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

gender_choices = ((True, 'male'), (False, 'female'))

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=10)
    birth_date = models.DateField(blank=True, null=True, editable=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='image/avatar')
    gender = models.CharField(blank=True, null=True, max_length=20, choices=gender_choices)
    address = models.TextField(blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    province = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


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