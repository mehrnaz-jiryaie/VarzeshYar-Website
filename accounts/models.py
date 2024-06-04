from django.db import models
import datetime

# from phonenumber_field.modelfields import PhoneNumberField


class Account(models.Model):
    """Represents an account for each person."""
    MALE = True
    FEMALE = False
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    MARRIED = True
    SINGLE = False
    MARITAL_STATUS_CHOICES = [
        (MARRIED, 'Married'),
        (SINGLE, 'Single'),
    ]

    username = models.CharField(unique=True, blank=False, max_length=100)
    password = models.CharField(blank=False, max_length=128)
    email = models.EmailField(max_length=254)
    confirm_password = models.CharField(blank=False, max_length=128)
    first_name = models.CharField(default='ali', max_length=100)
    last_name = models.CharField(default='alavi', max_length=100)
    # phone_number = PhoneNumberField(max_length=11, blank=True)
    birth_date = models.DateField(default=datetime.date.today)
    sex = models.BooleanField(choices=SEX_CHOICES, default=MALE)
    marital_status = models.BooleanField(
        choices=MARITAL_STATUS_CHOICES, default=SINGLE)
    weight = models.PositiveSmallIntegerField(default=40)
    height = models.FloatField(default=1.5)
    waist = models.FloatField(default=20)
    abdomen = models.FloatField(default=20)
    chest = models.FloatField(default=20)
    leg = models.FloatField(default=20)
    arm = models.FloatField(default=20)
    hip = models.FloatField(default=20)
    thigh = models.FloatField(default=20)
    shoulder = models.FloatField(default=20)
    
    

    def __str__(self):
        """A string that reperesent the account in Django admin."""
        return self.username
