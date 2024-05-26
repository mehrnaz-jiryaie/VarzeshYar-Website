from django import forms
from .models import Account
import hashlib


class AccountCreationForm(forms.ModelForm):
    # username = forms.CharField(label='Username', widget=forms.TextInput)
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    # email = forms.EmailField(label='Email', widget=forms.EmailInput)

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class LoginForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'password']
        
        
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     password = self.cleaned_data["password1"]
    #     # Hash the password using SHA-256
    #     hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    #     user.password = hashed_password
    #     if commit:
    #         user.save()
    #     return user