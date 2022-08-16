from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image','bio']
        # field

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']