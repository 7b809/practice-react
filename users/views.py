from django.shortcuts import render,redirect
# Create your views here.
from .models import Profile
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def loginPage(request):

    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request,"username does not exist")
    
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,'Username or password is incorrect')

    return render(request,'users/login_register.html')

def logoutUser(request):
    logout(request)
    request.session.flush()  # extra: ensures all session data is cleared
    messages.error(request,"username logged out.")

    return redirect('login')


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}

    return render(request,'users/profiles.html',context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {'profile': profile, 'topSkills': topSkills,
               "otherSkills": otherSkills}
    return render(request, 'users/user-profile.html', context)
