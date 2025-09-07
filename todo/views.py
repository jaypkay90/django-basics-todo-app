from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    # return HttpResponse("<h1>Add Task</h1>")
    if request.method == 'POST':
        if request.POST['task'].strip() != '':
            Task.objects.create(
                task = request.POST['task'],   
            )
    return redirect('home')
    