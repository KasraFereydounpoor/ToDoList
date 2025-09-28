from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

from django.utils import timezone

from django.utils import timezone

def task_list(request):
    tasks = Task.objects.all().order_by('-created_date')

    today = timezone.now().date()
    today_tasks = Task.objects.filter(created_date__date=today)
    completed_today = today_tasks.filter(completed=True).count()
    uncompleted_today = today_tasks.filter(completed=False).count()
    all_today = today_tasks.count()
    percent_today = int((completed_today / all_today) * 100) if all_today > 0 else 0


    context = {
        'tasks': tasks,
        'today_completed': completed_today,
        'today_uncompleted': uncompleted_today,
        'today_total': all_today,
        'percent_today': percent_today,
    }
    return render(request, 'app_todo/task_list.html', context)


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'app_todo/task_form.html', {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'app_todo/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'app_todo/task_confirm_delete.html', {'task': task})
