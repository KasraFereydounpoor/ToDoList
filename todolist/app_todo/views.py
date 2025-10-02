from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

from django.utils import timezone

from django.utils import timezone

def task_list(request):
    
    search_query = request.GET.get('search', '')
    order_mode = request.GET.get('order', '')
    
    
    print(f"search_query: {search_query}, order_mode: {order_mode}")
    tasks = Task.objects.all()
    
    tasks = Task.objects.all()
    if search_query:
        tasks = tasks.filter(title__icontains=search_query)
    if order_mode == "completed":
        tasks = tasks.order_by('-completed', '-created_date')
    elif order_mode == "not_completed":
        tasks = tasks.order_by('completed', '-created_date')
    else:
        tasks = tasks.order_by('-created_date')  # فقط یک بار این خط
    
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
        'show_dashboard': True,
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
    from django.utils import timezone
    today = timezone.now().date()
    today_tasks = Task.objects.filter(created_date__date=today)
    completed_today = today_tasks.filter(completed=True).count()
    uncompleted_today = today_tasks.filter(completed=False).count()
    all_today = today_tasks.count()
    percent_today = int((completed_today / all_today) * 100) if all_today > 0 else 0

    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'app_todo/task_confirm_delete.html', {
        'task': task,
        'today_completed': completed_today,
        'today_uncompleted': uncompleted_today,
        'today_total': all_today,
        'percent_today': percent_today,
    })



def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()
    return redirect('task_list')

def task_uncomplete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = False
    task.save()
    return redirect('task_list')
