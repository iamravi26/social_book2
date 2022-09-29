
from asyncio.windows_events import NULL
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,User,PermissionsMixin

# Create your models here.

class CustomUserManager(BaseUserManager):
    
    def create_user(self,email,first_name,last_name,password):

        if not email:
            raise ValueError('User must have email')
        
        if not first_name:
            raise ValueError('Enter your first name')

        user= self.model(
            email=self.normalize_email(email=email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(raw_password=password)
        user.save(using=self.db)

        return user
    
    def create_superuser(self,email,first_name,last_name,password):

        user=self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password
            )
        user.is_admin=True 
        user.is_staff=True    
        user.is_superuser=True

        user.save(using=self.db)

        return user




class CustomUser(AbstractBaseUser,PermissionsMixin):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    password=models.CharField(max_length=100)
    username=models.CharField(max_length=100,verbose_name="enter your username",default=None,unique=True,null=True)
    first_name=models.CharField(max_length=100,verbose_name="enter your first name")
    last_name=models.CharField(max_length=100,verbose_name="enter your last name")
    email=models.EmailField(max_length=150,verbose_name="enter your email address",unique=True)
    public_visibility = models.BooleanField(default=True)
    author = models.BooleanField(default=False,null=True)
    seller = models.BooleanField(default=False,null=True)
    # datetime = models.DateTimeField(auto_now=True)
    date_of_birth = models.DateField(auto_now_add=False, null = True)
    # age = models.IntegerField(blank=True, null=True)
    Address = models.TextField(max_length=300, null = True,verbose_name='enter your address')
    is_active=models.BooleanField(default=True) #to allow user to login if do False it wont be allowed to login
    is_admin=models.BooleanField(default=False) 
    is_staff=models.BooleanField(default=False)    
    is_superuser=models.BooleanField(default=False)  


    objects=CustomUserManager()  

    REQUIRED_FIELDS=['first_name','last_name']

    USERNAME_FIELD='username'
    EMAIL_FIELD='email'

    def __str__(self):
        return self.username

    def __str__(self):
        return self.email

    def get_first_name(self):
        return self.first_name
   
    def get_last_name(self):
            return self.last_name





# class CustomUser(models.Model):
#     name=models.CharField(max_length=150)
#     username=models.CharField(max_length=150)
#     email=models.EmailField(max_length=150)
#     password=models.CharField(max_length=150)

