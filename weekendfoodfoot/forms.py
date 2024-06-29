# forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'password2': 'Confirm password',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Notez le changement ici, utilisez super() au lieu de super(MyUserCreationForm, self)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})