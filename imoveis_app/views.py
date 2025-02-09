from django.shortcuts import render, redirect
from .models import User, Casa
from django.contrib.auth import authenticate, login, logout
from .forms import MyuserCreationForm, CasasForms
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    casas = Casa.objects.all()
    return render(request,'im_templates/home.html', {'casas':casas})

def login_page(request):
    page = 'login'
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email= email)
            user.is_authenticated
        except:
            print('user not found lol')
        user = authenticate(request,username = email, password = password)
    
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('something went wrong with login form')

    return render(request, 'im_templates/login.html', {'page':page})

def exit_page(request):
    logout(request)
    return redirect('home')

def register_user(request):
    form = MyuserCreationForm()
    if request.method == "POST":
        form = MyuserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            print('something went wrong with register user.')
    return render(request, 'im_templates/login.html', {'form':form})

@login_required(login_url= 'login')
def register_casa(request):
    form = CasasForms()
    user = request.user
    if request.method == 'POST':
        form = CasasForms(request.POST)
        if form.is_valid():
            casa = form.save(commit= False)
            casa.vendedor = user
            casa.save()
            return redirect('home')
        else:
            print('there was a problem with the casa form')
    return render(request, 'im_templates/register_casa.html', {'form':form})

