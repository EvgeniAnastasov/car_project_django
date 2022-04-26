from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import PasswordInput

from cars.accounts.models import Profile

UserModel = get_user_model()


class LoginForm(forms.Form):
    user = None
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'type': 'email',
                   'placeholder': 'Enter Your Email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'type': 'password',
                   'placeholder': 'Enter Your Password'}
        ),
    )

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Email and/or password incorect!')

    def save(self):
        return self.user


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("email", )

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter Your Email'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Enter Your Password'})
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder': 'Repeat Your Password'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

        exclude = ('user', 'total_cars', )

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'nationality': 'Nationality',
            'total_cars': 'Total Cars',
            'profile_image': 'Profile Image',
        }
