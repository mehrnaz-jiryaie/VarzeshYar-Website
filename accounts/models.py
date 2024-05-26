from django.db import models


class Account(models.Model):
    """Represents an account for each person."""
    username = models.CharField(unique=True, blank=False, max_length=100)
    password = models.CharField(blank=False, max_length=128)
    email = models.EmailField(max_length=254)
    confirm_password = models.CharField(blank=False, max_length=128)
    
    def __str__(self): 
        """A string that reperesent the account in Django admin."""   
        return self.username

    