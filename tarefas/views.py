from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
def home(request):
    tasks = Task.objects.all()
    total_tasks = len(tasks)
    completed_tasks = 0
    remaining_tasks = 0
    pct = 0
    return render(request,'tarefas/home.html')
