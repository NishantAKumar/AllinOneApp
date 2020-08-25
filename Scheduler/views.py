from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib import messages
# login function yet to be included
# db model yet to be created
events = []


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
