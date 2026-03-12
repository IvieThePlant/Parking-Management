from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#Override the default registration form to include email input.
class RegisterForm(UserCreationForm):
    name = forms.CharField(label="Name", max_length=100)
    username = forms.CharField(label="Username", max_length=100)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["name", "username", "email", 'password1', 'password2']