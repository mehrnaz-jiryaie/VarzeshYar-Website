from django import forms
from .models import Account
from django.core.exceptions import ValidationError


class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean(self):
        """Checks if the password and confirm password are equal."""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError(
                '* پسوردها یکسان نیستند، دوباره تلاش کنید.')

        return cleaned_data


class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'password']
