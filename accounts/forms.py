from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Account
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        error_messages={
            'required': 'لطفا ایمیل خود را وارد کنید.',
            'invalid': 'لطفا یک ایمیل معتبر وارد کنید.'
        }
    )
    username = forms.CharField(
        required=True,
        error_messages={
            'required': 'لطفا نام کاربری خود را وارد کنید.',
            'unique': 'این نام کاربری قبلا ثبت شده است.'
        }
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        error_messages={
            'required': 'لطفا رمز عبور خود را وارد کنید.',
        }
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
        error_messages={
            'required': 'لطفا تایید رمز عبور را وارد کنید.',
        }
    )

    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('رمزهای عبور مطابقت ندارند.')
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Account.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل قبلا ثبت شده است.')
        return email


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='نام کاربری',
        error_messages={
            'required': 'لطفا نام کاربری خود را وارد کنید.'
        }
    )
    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput,
        error_messages={
            'required': 'لطفا رمز عبور خود را وارد کنید.'
        }
    )

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                'این حساب کاربری غیر فعال است.',
                code='inactive',
            )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    'لطفا نام کاربری و رمز عبور صحیح را وارد کنید. توجه داشته باشید که هر دو فیلد ممکن است حساس به حروف باشند.',
                    code='invalid_login',
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number',
                  'email', 'birth_date', 'sex', 'marital_status']
        
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if Account.objects.filter(email=email).exists():
    #         raise forms.ValidationError('این ایمیل قبلا ثبت شده است.')
    #     return email
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ProfileForm, self).__init__(*args, **kwargs)

    def clean_email(self):
        email1 = self.cleaned_data.get('email')
        
        if self.request and self.request.user.is_authenticated:
            username = self.request.user.username
            account = Account.objects.filter(username=username).first()
            if account:
                email2 = account.email
                if email1 == email2:
                    return email1
                else:
                    raise forms.ValidationError('این ایمیل قبلا ثبت شده است.')
            else:
                raise forms.ValidationError('کاربری با این نام کاربری وجود ندارد.')
        else:
            raise forms.ValidationError('کاربر معتبر نیست.')

        return email1


class PhysicalInformationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['weight', 'height', 'waist', 'abdomen',
                  'chest', 'leg', 'arm', 'hip', 'thigh', 'shoulder']
    