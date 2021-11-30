from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Base(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract=True

class Account(Base):
    user = models.OneToOneField(User, related_name="account_user", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=150)


    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.email


    
