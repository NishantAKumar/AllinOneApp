from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from .models import MyAccountManager, User
# login function yet to be included
# db model yet to be created
events = []

def logout(request):
    auth.logout(request)
    return redirect ("/")

def login(request):
    if request.method == 'GET':
        return render(request, 'Scheduler/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("/login")

def register(request):
    if request.method == 'GET':
        return render(request, 'Scheduler/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirmation')

        if password == confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(password=password, email=email, username=username)
                return redirect('/login')
        else:
            messages.info(request, 'Passwords Do Not Match')
            return redirect('/register')
        
def options(request):
    return render(request, 'Scheduler/options.html')

def create(request):
    if request.method == 'GET':
        return render(request, 'Scheduler/create.html')
    else:
        events.append(f'Date: {request.POST.get("event_date")} | Description: {request.POST.get("event_des")}')
        messages.info(request, 'Event Created')
        return redirect('/create')

def read(request):
    if len(events) > 0 :
        return render(request, 'Scheduler/read.html', context={'events': events}) #Read function will always receive get requests
    else:
        return render(request, 'Scheduler/read.html')

def update(request):
    if request.method == 'GET':
        return render(request, 'Scheduler/update.html', context={'events': events})
    else:
        for i in range(len(events)):
            if f'Date: {request.POST.get("key2")} | Description: {request.POST.get("key1")}' == events[i]:
                events[i] = f'Date: {request.POST.get("new_date")} | Description: {request.POST.get("new_des")}'
                messages.info(request, 'Event Updated')
            print(events, i)
        return redirect('update')
        
def delete(request):
    if request.method == 'GET':
        return render(request, 'Scheduler/delete.html', context={'events': events})
    else:
        for i in events:
            if f'Date: {request.POST.get("key2")} | Description: {request.POST.get("key1")}' == i:
                events.remove(i)
                messages.info(request, 'Event Deleted')
        return redirect('delete')

def profile(request):
    return render(request, 'Scheduler/profile.html')