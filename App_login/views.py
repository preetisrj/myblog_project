from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_login.forms import Signupform, Userprofilechange, ProfilePic

# Create your views here.


def sign_up(request):
    form = Signupform()
    registered = False
    if request.method == 'POST':
        form = Signupform(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'form':form,'registered':registered}   
    return render(request, 'App_login/signup.html',context=dict)

def login_page(request):
    form = AuthenticationForm()
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'App_login/login.html',context={'form':form})


@ login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_login:signin'))


@ login_required
def profile(request):
    return render(request, 'App_login/profile.html', context={})


@ login_required
def user_change(request):
    current_user = request.user
    change = False
    form = Userprofilechange(instance=current_user )
    
    if request.method == 'POST':
        form = Userprofilechange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = Userprofilechange(instance=current_user)
            change = True
    return render(request,'App_login/change_profile.html',context={'form':form,'change':change})


@ login_required
def pass_change(request):
    current_user = request.user
    passw=False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user,data=request.POST)
        if form.is_valid():
            form.save()
            passw =True
    return render (request,'App_login/pass_change.html',context={'form':form,'passw':passw})


@ login_required
def addprofile_pic(request):
    form = ProfilePic()
    if request.method =='POST':
        form = ProfilePic(request.POST,request.FILES)
        
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_login:profile'))

    return render(request,'App_login/addprofile_pic.html',context={'form':form})

@login_required
def change_pro_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method =='POST':
        form = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_login:profile'))
    return render(request, 'App_login/addprofile_pic.html', context={'form': form})
