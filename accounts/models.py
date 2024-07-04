from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class Account(AbstractUser):
    """Represents an Account for each person."""
    class Meta:
        verbose_name = "Athlete"
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
        if Account.objects.filter(email=self.email).exclude(pk=self.pk).exists() or \
           TrainerAccount.objects.filter(email=self.email).exclude(pk=self.pk).exists():
            raise ValidationError({'email': 'این ایمیل قبلا ثبت شده است.'})
        if Account.objects.filter(username=self.username).exclude(pk=self.pk).exists() or \
           TrainerAccount.objects.filter(username=self.username).exclude(pk=self.pk).exists():
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

    dumbbell_pair_squat_reps = models.IntegerField(blank=True, null=True)
    dumbbell_pair_squat_sets = models.IntegerField(blank=True, null=True)

    inside_the_thigh_wire_reps = models.IntegerField(blank=True, null=True)
    inside_the_thigh_wire_sets = models.IntegerField(blank=True, null=True)

    back_of_the_thigh_wired_reps = models.IntegerField(blank=True, null=True)
    back_of_the_thigh_wired_sets = models.IntegerField(blank=True, null=True)

    fly_reps = models.IntegerField(blank=True, null=True)
    fly_sets = models.IntegerField(blank=True, null=True)

    cross_over_reps = models.IntegerField(blank=True, null=True)
    cross_over_sets = models.IntegerField(blank=True, null=True)

    french_triceps_reps = models.IntegerField(blank=True, null=True)
    french_triceps_sets = models.IntegerField(blank=True, null=True)

    two_sided_bending_publication_reps = models.IntegerField(
        blank=True, null=True)
    two_sided_bending_publication_sets = models.IntegerField(
        blank=True, null=True)

    fly_back_reps = models.IntegerField(blank=True, null=True)
    fly_back_sets = models.IntegerField(blank=True, null=True)

    crunch_reps = models.IntegerField(blank=True, null=True)
    crunch_sets = models.IntegerField(blank=True, null=True)

    climber_reps = models.IntegerField(blank=True, null=True)
    climber_sets = models.IntegerField(blank=True, null=True)

    front_thigh_reps = models.IntegerField(blank=True, null=True)
    front_thigh_sets = models.IntegerField(blank=True, null=True)

    seated_hip_trust_reps = models.IntegerField(blank=True, null=True)
    seated_hip_trust_sets = models.IntegerField(blank=True, null=True)

    free_dumbbell_kickback_reps = models.IntegerField(blank=True, null=True)
    free_dumbbell_kickback_sets = models.IntegerField(blank=True, null=True)

    double_barbell_chest_reps = models.IntegerField(blank=True, null=True)
    double_barbell_chest_sets = models.IntegerField(blank=True, null=True)

    military_chest_on_the_upper_chest_reps = models.IntegerField(
        blank=True, null=True)
    military_chest_on_the_upper_chest_sets = models.IntegerField(
        blank=True, null=True)

    single_arm_dumbbell_shoulder_reps = models.IntegerField(
        blank=True, null=True)
    single_arm_dumbbell_shoulder_sets = models.IntegerField(
        blank=True, null=True)

    hand_open_boat_reps = models.IntegerField(blank=True, null=True)
    hand_open_boat_sets = models.IntegerField(blank=True, null=True)

    plank_reps = models.IntegerField(blank=True, null=True)
    plank_sets = models.IntegerField(blank=True, null=True)

    belly_roll_reps = models.IntegerField(blank=True, null=True)
    belly_roll_sets = models.IntegerField(blank=True, null=True)

    parallel_abdomen_reps = models.IntegerField(blank=True, null=True)
    parallel_abdomen_sets = models.IntegerField(blank=True, null=True)

    outer_thigh_wire_reps = models.IntegerField(blank=True, null=True)
    outer_thigh_wire_sets = models.IntegerField(blank=True, null=True)

    standing_leg_reps = models.IntegerField(blank=True, null=True)
    standing_leg_sets = models.IntegerField(blank=True, null=True)

    hello_japanese_on_high_reps = models.IntegerField(blank=True, null=True)
    hello_japanese_on_high_sets = models.IntegerField(blank=True, null=True)

    single_arm_chest_reps = models.IntegerField(blank=True, null=True)
    single_arm_chest_sets = models.IntegerField(blank=True, null=True)

    triceps_wire_reps = models.IntegerField(blank=True, null=True)
    triceps_wire_sets = models.IntegerField(blank=True, null=True)

    full_body_barbell_shoulder_strap_reps = models.IntegerField(
        blank=True, null=True)
    full_body_barbell_shoulder_strap_sets = models.IntegerField(
        blank=True, null=True)

    pull_face_reps = models.IntegerField(blank=True, null=True)
    pull_face_sets = models.IntegerField(blank=True, null=True)

    russian_turn_reps = models.IntegerField(blank=True, null=True)
    russian_turn_sets = models.IntegerField(blank=True, null=True)

    russian_side_reps = models.IntegerField(blank=True, null=True)
    russian_side_sets = models.IntegerField(blank=True, null=True)

    lower_abdomen_90_degrees_reps = models.IntegerField(blank=True, null=True)
    lower_abdomen_90_degrees_sets = models.IntegerField(blank=True, null=True)


class TrainerAccount(AbstractUser):
    """Represents a TrainerAccount Account."""
    class Meta:
        verbose_name = "Trainer"
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
        if TrainerAccount.objects.filter(email=self.email).exclude(pk=self.pk).exists() or \
           Account.objects.filter(email=self.email).exclude(pk=self.pk).exists():
            raise ValidationError({'email': 'این ایمیل قبلا ثبت شده است.'})
        if TrainerAccount.objects.filter(username=self.username).exclude(pk=self.pk).exists() or \
           Account.objects.filter(username=self.username).exclude(pk=self.pk).exists():
            raise ValidationError(
                {'username': 'این نام کاربری قبلا ثبت شده است.'})

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    specialty = models.CharField(max_length=100, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
