from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class Account(AbstractUser):
    """Represents an account for each person."""
    username = models.CharField(unique=True, blank=False, max_length=10)
    email = models.EmailField(unique=True, max_length=254)

    def __str__(self):
        """A string that represents the account in Django admin."""
        return self.username

    def clean(self):
        if Account.objects.filter(email=self.email).exclude(pk=self.pk).exists():
            raise ValidationError(
                {'email': 'این ایمیل قبلا ثبت شده است.'})
        if Account.objects.filter(username=self.username).exclude(pk=self.pk).exists():
            raise ValidationError(
                {'username': 'این نام کاربری قبلا ثبت شده است.'})

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

    # owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    # first_name = models.CharField(default='ali', max_length=100)
    # last_name = models.CharField(default='alavi', max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, choices=[(
        'M', 'Male'), ('F', 'Female')], blank=True, null=True)
    marital_status = models.CharField(max_length=10, choices=[(
        'single', 'Single'), ('married', 'Married')], blank=True, null=True)
    weight = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    waist = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    abdomen = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    chest = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    leg = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    arm = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    hip = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    thigh = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
    shoulder = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True)
