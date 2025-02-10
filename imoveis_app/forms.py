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



class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class ImageForm(forms.ModelForm):
    images = MultipleFileField(label='Selecione as imagens', required=False)

    class Meta:
        model = ImageCasa
        fields = []