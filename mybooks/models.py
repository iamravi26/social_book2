
from asyncio.windows_events import NULL
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,User,PermissionsMixin

# Create your models here.

# class CustomUserManager(BaseUserManager):

#     use_in_migrations=True
    
#     def create_user(self,email,password=None,**extra_fields):

#         if not email:
#             raise ValueError('User must have email')

#         # if not username:
#         #     raise ValueError('User must have username')
        
#         # if not first_name:
#         #     raise ValueError('Enter your first name')
#         email=self.normalize_email(email)
#         user= self.model(email=email,**extra_fields)
#         user.set_password(raw_password=password)
#         user.save(using=self.db)

#         return user
    
#     def create_superuser(self,email,password,**extra_fields):

#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_active',True)
#         extra_fields.setdefault('is_superuser',True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('superuser must have is_staff True')

#         return self.create_user(email,password,**extra_fields)



        # user=self.create_user(
        #     email=email,
        #     first_name=first_name,
        #     last_name=last_name,
        #     password=password
        #     )
        # # user.is_admin=True 
        # # user.is_staff=True    
        # # user.is_superuser=True

        # user.save(using=self.db)

        # return user




class CustomUser(AbstractUser,PermissionsMixin):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    username=None
    # password=models.CharField(max_length=100)
    # username=models.CharField(max_length=100,verbose_name="enter your username",default=None,unique=True,null=True)
    # first_name=models.CharField(max_length=100,verbose_name="enter your first name")
    # last_name=models.CharField(max_length=100,verbose_name="enter your last name")
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

    REQUIRED_FIELDS=[]

    USERNAME_FIELD='email'
    # EMAIL_FIELD='email'

    # def __str__(self):
    #     return self.username

    # def __str__(self):
    #     return self.email

    # def get_first_name(self):
    #     return self.first_name
   
    # def get_last_name(self):
    #         return self.last_name





# class CustomUser(models.Model):
#     name=models.CharField(max_length=150)
#     username=models.CharField(max_length=150)
#     email=models.EmailField(max_length=150)
#     password=models.CharField(max_length=150)

