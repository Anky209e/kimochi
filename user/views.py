from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User
from .forms import ProfileForm,RegisterForm


def profile(request,username):
    current_user = request.user
    user = User.objects.get(username=username)
    
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        if request.FILES:
            image = request.FILES.get("profile_image")
            profile.profile_image = image
        bio = request.POST.get("bio")
        profile.bio = bio
        profile.save()

    
    if user == current_user:
        profile_form = ProfileForm(instance=profile)
        context = {
            "user" : user,
            "profile" : profile,
            "profile_form" : profile_form,
            "owner" : True
        }
    else:
        context = {
            "user" : user,
            "profile" : profile,
            "owner" : False
        }
    
        

    return render(request,"registration/profile.html",context)

def register_account(request):
    form = RegisterForm()

    context = {
        "form":form
    }
    return render(request,"registration/register.html",context)
