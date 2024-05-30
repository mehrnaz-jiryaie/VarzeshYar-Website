from django import forms
from .models import Account
from django.core.exceptions import ValidationError


class AccountCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # Username validation
        if Account.objects.filter(username=username).exists():
            self.add_error(
                'username', "این نام کاربری قبلاً گرفته شده است. لطفا یکی دیگر را وارد کنید.")

        # Password validation
        if password:
            if len(password) < 8:
                self.add_error(
                    'password', "رمز عبور شما باید دارای حداقل 8 کاراکتر باشد.")

        # Confirm password validation
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password',
                           "پسوردها یکسان نیستند، دوباره تلاش کنید.")

        return cleaned_data
    # class Meta:
    #     model = Account
    #     fields = ['username', 'email', 'password', 'confirm_password']

    # def clean_username(self):
    #     """Checks if the username is unique."""
    #     username = self.cleaned_data.get('username')
    #     if Account.objects.filter(username=username).exists():
    #         raise ValidationError(
    #             'این نام کاربری قبلاً گرفته شده است. لطفا یکی دیگر را وارد کنید.')
    #     return username

    # def clean(self):
    #     """Checks if password and confirm password are equal."""
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     confirm_password = cleaned_data.get('confirm_password')

    #     if password != confirm_password:
    #         raise ValidationError('پسوردها یکسان نیستند، دوباره تلاش کنید.')
    #     return cleaned_data

    # def clean_password(self):
    #     """Checks if password length is more than or equal 8 characters."""
    #     password = self.cleaned_data.get('password')

    #     if password and len(password) < 8:
    #         raise ValidationError(
    #             'رمز عبور شما باید دارای حداقل 8 کاراکتر باشد.')
    #     return password


class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'password']
