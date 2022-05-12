from django.forms import ModelForm
from .models import auth_user
from django.contrib.auth.models import User


class user_form(ModelForm):
    class Meta:
        model = auth_user
        fields = ['avatar']

class user_user(ModelForm):
    class Meta:
        model = User
        fields = ["username",'email', 'password']

