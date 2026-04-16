from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#Override the default registration form to include email input.
class RegisterForm(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 outline-gray-300'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 outline-gray-300'
    }))

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 outline-gray-300'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['password1', 'password2']:
            self.fields[field].widget.attrs.update({
                'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 outline-gray-300'
            })