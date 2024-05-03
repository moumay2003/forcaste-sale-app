from django.shortcuts import render, redirect
from mouh2.form import NumberForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from mouh2.models import Message
from mouh2.form import MessageForm
# Create your views here.
def index(request):
    return render(request, 'index.html')


def stat(request):
    return render(request, 'stat.html')


def image_viewer(request):
    form = NumberForm()
    return render(request, 'stat.html', {'form': form})

def display_image(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            context = {'number': number}
            return render(request, 'displayimg.html', context)
    else:
        form = NumberForm()
    return render(request, 'stat.html', {'form': form})


def loginPage(request) :
    page='log'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try :
            user= User.objects.get(username=username)
        except :
            messages.error(request, "User does not exist.")
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password is incorrect.")   

                
    context = {'page': page}    
    return render(request, 'log.html',context)


def logoutUser(request):
    logout(request)
    return redirect('log')

def registerPage(request) :
    page='register'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('log')
        else :
            messages.error(request, "An error occured during registration.")
    return render(request, 'log.html', {'form': form})


@login_required
def chat_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.username = request.user
            message.save()
            return redirect('chat')
    else:
        form = MessageForm()
    messages = Message.objects.all().order_by('-created')[:50]
    return render(request, 'chatroom.html', {'messages': messages, 'form': form})


def predict(request):
    form = NumberForm()
    return render(request, 'predict.html', {'form': form})

def display_image2(request):
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            context = {'number': number}
            return render(request, 'displayimg2.html', context)
    else:
        form = NumberForm()
    return render(request, 'predict.html', {'form': form})