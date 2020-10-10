from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth.models import auth
from .models import MyAccountManager, User, TodoList
from Scheduler.NewsApi import NewsFinder
from .serializers import TodoSerializer, UserSerializer
from rest_framework.decorators import api_view
from Scheduler.youtubeSearch import search

def logout(request):
    auth.logout(request)
    return redirect ("login")

def login(request):
    if request.method == 'GET':
        return render(request, 'Scheduler/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("options")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")

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
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(password=password, email=email, username=username)
                return redirect('login')
        else:
            messages.info(request, 'Passwords Do Not Match')
            return redirect('register')
        
def options(request):
    return render(request, 'Scheduler/options.html')

def create(request):
    if request.method == 'POST' and request.POST.get("event_des") != "":
        user = User.objects.get(username=request.user)
        create = TodoList.objects.create(description=request.POST.get("event_des"), user=user)
        messages.info(request, 'Event Created')
        return redirect('read')
    else:
        messages.info(request, 'Description Cannot Be Blank')
        return redirect('read')

def read(request):
    all_to_dos = User.objects.get(username=request.user).todolist_set.all()
    return render(request, 'Scheduler/read.html', context={'data': all_to_dos})


def update(request, updation_id):
    if request.method == 'POST' and (request.POST.get("updation")).replace(" ", "") != "":
        updation_item = TodoList.objects.get(id = updation_id)
        updation_item.description = request.POST.get("updation")
        updation_item.save()
        messages.info(request, 'Event Updated')
        return redirect("read")
    else:
        messages.info(request, 'The Update Cannot Be Blank')
        return redirect('read')

def delete(request, deletion_id):
    if request.method == 'POST':
        deletion_item = TodoList.objects.get(id=deletion_id)
        deletion_item.delete()
        messages.info(request, 'Event Deleted')
        return redirect('read')

def profile(request):
    return render(request, 'Scheduler/profile.html')

def AccDelete(request):
    if request.method == "POST":
        check = auth.authenticate(username=request.user, password=request.POST.get('password'))
        if check:
            s = User.objects.get(username=request.user)
            s.delete()
            messages.info(request, 'Account Deleted')
            return redirect('login')
    
    else:
        return render(request, 'Scheduler/accdelete.html')

def news(request):
    if request.method == 'GET':
        return render(request, 'Scheduler/News.html')
    else:
        option = request.POST.get('option')
        news_pack = NewsFinder(option.upper())
        return render(request, 'Scheduler/NewsOutput.html', context={"data_pack" : news_pack, "option":option})

#api related views
@api_view(['GET'])
def taskList(request):
    tasks = User.objects.get(username=request.user).todolist_set.all()
    serializer = TodoSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def taskData(request):
    if request.user.is_admin:
        tasks = TodoList.objects.all()
        serializer = TodoSerializer(tasks, many = True)
        return Response(serializer.data)
    else:
        return HttpResponse("<H3>Unauthorized</H3>")

@api_view(['GET'])
def UserList(request):
    if request.user.is_admin:
        tasks = User.objects.all()
        serializer = UserSerializer(tasks, many = True)
        return Response(serializer.data)

    else:
        return HttpResponse("<H3>Unauthorized</H3>")

@api_view(['POST'])
def taskCreate(request):
    serializer = TodoSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = User.objects.get(username=request.user).todolist_set.get(id=pk)
    serializer = TodoSerializer(instance = tasks, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    tasks = User.objects.get(username=request.user).todolist_set.get(id=pk)
    tasks.delete()
    return Response("Item has been deleted")

def youtube(request):
    if request.method == 'GET':
        return render(request, 'Scheduler/youtube_search.html')
    elif request.method == 'POST':
        return render(request, 'Scheduler/youtube_search.html', {'videos':search(request.POST.get('query'))})