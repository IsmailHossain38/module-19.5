from django import forms 
from . models import AlbumModel
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models  import User

class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields ="__all__"
        
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields =['username','first_name','last_name','email']