from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, AbstractUser
import random, string

class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError("Users must have an email address")
        
        user = self.model(phone=phone)
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone, password=None):
        user = self.create_user(
            phone,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser):
    phone = models.CharField(verbose_name='Phone Number', max_length=11, unique=True)
    first_name = models.CharField(verbose_name='First Name', max_length=20, blank=True, null=True)
    last_name= models.CharField(verbose_name='Last Name', max_length=20, blank=True, null=True)
    
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = "phone"
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    

class Wallet(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='wallet')
    balance = models.PositiveBigIntegerField(verbose_name="Balance",default=0)
    
    def __str__(self):
        return f'{self.user} Wallet'