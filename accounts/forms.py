from django import forms
from .models import Account


class AccountCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
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


class LoginForm(forms.Form):
    
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if username and password:
            if Account.objects.filter(username=username).exists():
                account = Account.objects.get(username=username)
                if account.password != password:
                    self.add_error('password', "رمز عبور نادرست است.")
            else:
                self.add_error('username', "نام کاربری نادرست است.")

        return cleaned_data
