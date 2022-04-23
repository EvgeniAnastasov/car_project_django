from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from cars.accounts.models import Profile

UserModel = get_user_model()


class LoginForm(forms.Form):
    user = None
    email = forms.EmailField(
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
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


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

        exclude = ('user', )

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'nationality': 'Nationality',
            'total_cars': 'Total Cars',
            'profile_image': 'Profile Image',
        }
