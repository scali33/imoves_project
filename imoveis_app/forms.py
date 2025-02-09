from django.contrib.auth.forms import UserCreationForm
from .models import User, Casa
from django.forms import ModelForm

class MyuserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class CasasForms(ModelForm):
    class Meta:
        model = Casa
        fields = '__all__'
        exclude = ['vendedor']