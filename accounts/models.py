from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class Account(AbstractUser):
    """Represents an Account for each person."""
    username = models.CharField(unique=True, blank=False, max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='athlete_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='athlete_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        """A string that represents the Account in Django admin."""
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


class TrainerAccount(AbstractUser):
    """Represents a TrainerAccount Account."""
    username = models.CharField(unique=True, blank=False, max_length=100)
    email = models.EmailField(unique=True, max_length=254)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='TrainerAccount_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='TrainerAccount_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        """A string that represents the TrainerAccount in Django admin."""
        return self.username

    def clean(self):
        if TrainerAccount.objects.filter(email=self.email).exclude(pk=self.pk).exists():
            raise ValidationError(
                {'email': 'این ایمیل قبلا ثبت شده است.'})
        if TrainerAccount.objects.filter(username=self.username).exclude(pk=self.pk).exists():
            raise ValidationError(
                {'username': 'این نام کاربری قبلا ثبت شده است.'})

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, choices=[
        ('M', 'Male'), ('F', 'Female')
    ], blank=True, null=True)
    marital_status = models.CharField(max_length=10, choices=[
        ('single', 'Single'), ('married', 'Married')
    ], blank=True, null=True)
    specialty = models.CharField(max_length=100, blank=True, null=True)
    experience_years = models.PositiveIntegerField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
