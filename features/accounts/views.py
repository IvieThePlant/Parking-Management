from django.shortcuts import render

# Create your views here.
#Import default
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm

from django.contrib.auth.forms import AuthenticationForm

class StyledAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'block w-full rounded-md bg-white px-3 py-2 text-gray-900 text-sm outline outline-1 outline-gray-300'
            })

#Override register function to redirect user to specific pages.
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/accounts/login')
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})