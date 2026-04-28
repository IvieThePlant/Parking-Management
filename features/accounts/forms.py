from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

input_class = 'block w-full rounded-md bg-white px-3 py-2 text-gray-900 text-sm outline outline-1 outline-gray-300'

class RegisterForm(UserCreationForm):
    name = forms.CharField(label="Name", max_length=100, widget=forms.TextInput(attrs={'class': input_class}))
    username = forms.CharField(label="Username", max_length=100, widget=forms.TextInput(attrs={'class': input_class}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': input_class}))

    class Meta:
        model = User
        fields = ["name", "username", "email", 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': input_class})
        self.fields['password2'].widget.attrs.update({'class': input_class})