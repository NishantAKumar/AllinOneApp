from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        user = self.model(email =  self.normalize_email(email), username = username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email , password=None):
        user = self.create_user(email =  self.normalize_email(email), password = password, username = username)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email                                      = models.EmailField(unique=True)
    username                                   = models.CharField(max_length = 30, unique=True)
    is_admin                                   = models.BooleanField(default=False)
    is_superuser                               = models.BooleanField(default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager() 

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perm(self, app_label):
        return True