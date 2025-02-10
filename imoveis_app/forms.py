from django.contrib.auth.forms import UserCreationForm
from .models import User, Casa, ImageCasa
from django.forms import ModelForm
from django import forms

class MyuserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'numero','password1', 'password2']

class CasasForms(ModelForm):
    class Meta:
        model = Casa
        fields = '__all__'
        exclude = ['vendedor']



class UploadFilesForm(forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'allow_multiple_selected': True}))