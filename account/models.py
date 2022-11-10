from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
class MyAccountManager(BaseUserManager):

    # creating a user for our admin
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('Email is missing, user must have email')
        if not username:
            raise ValueError('Username missing')
        user = self.model(
            email=self.normalize_email(email),  # lower case email
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # creating a super user once the user have been created
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

# Create your models here.
class Account(models.Model):
    first_Name=models.CharField(max_length=200, unique=True)
    last_Name=models.CharField(max_length=200, unique=True)
    user_Name=models.CharField(max_length=200, unique=True)
    dOB=models.IntegerField(null=True)
    email=models.EmailField(max_length=200, unique=True)
    password=models.CharField(max_length=200, unique=True)

# requiered mandatory when creating a custom user model
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
     
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["user_Name, first_Name, last_Name"]

    objects = MyAccountManager()

    def str(self):
        return self.email

# if the user is the admin, he can make changes
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True

