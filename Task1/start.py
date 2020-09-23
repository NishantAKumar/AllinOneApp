from django.shortcuts import render

def startPage(request):
    return render(request, 'Task1/Task1/start.html')