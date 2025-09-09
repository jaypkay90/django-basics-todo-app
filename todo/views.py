from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
# Fast alles views verändern unmittelbar die Daten in der DB
# Daher sollten POST-Requests verwendet werden
# GET ist nur zum Anzeigen/Lesen da
# POST ist für Änderungen da
# Beispiel: Würde man die delete-Funktion über GET implementieren, 
# könnte jeder durch die entsprechende URL einen Task löschen

@require_POST
def addTask(request):
    # return HttpResponse("<h1>Add Task</h1>")
    if request.POST['task'].strip() != '':
        Task.objects.create(
            task = request.POST['task'],   
        )
    return redirect('home')

@require_POST
def completeTask(request, task_id):
    # task_qs = Task.objects.filter(id=task_id)
    # if task.exists():
    #     Task.objects.filter(id=task_id).update(is_completed=True)
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('home')

@require_POST
def deleteTask(request, task_id):
    # task_qs = Task.objects.filter(id=task_id)
    # if task_qs.exists():
    #     task_qs.delete()
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')

@require_POST
def markTaskUndone(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = False
    task.save()
    return redirect('home')


def editTask(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        if request.POST['task'].strip() != '':
            task.task = request.POST['task']
            task.save()
        return redirect('home')
    else:
        return render(request, 'editTask.html', {'task': task})