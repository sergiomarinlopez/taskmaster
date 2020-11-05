import os
import datetime

from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q

from todo.models import Task, Project
from todo.forms import ProjectModelForm

def homepage(request):
    return render(request, 'todo/homepage.html', {
        "tasks": Task.objects.all().order_by('-created')[0:3],
        })


def hola(request):
    return render(request, 'todo/hola.html', {
        "now": datetime.datetime.now(),
    })


def numero(request, num):
    m = dict(enumerate([
        "cero", "uno", "dos", "tres", "cuatro",
        "cinco", "seis", "siete", "ocho", "nueve",
    ]))
    return render(request, "todo/numero.html", {
        "resultado": m.get(num, "muchos"),
    })


def files(request):
    all_files = list(os.listdir("todo"))
    all_sizes = [
        os.path.getsize(os.path.join("todo", f))
        for f in all_files
    ]
    return render(request, 'todo/files.html', {
        'items': list(zip(all_files, all_sizes)),
        "max_size": max(all_sizes),
    })


def tareas(request):
    return render(request, 'todo/tareas.html', {
        "tareas": Task.objects
            .select_related('project')
            .order_by('-created')
            .all(),
    })


def detalle_tarea(request, id_tarea):
    return render(request, 'todo/detalle_tarea.html', {
        'task':  Task.objects.get(pk=id_tarea)
        })


def proyectos(request):
    return render(request, 'todo/proyectos.html', {
        "proyectos": Project.objects.all(),
    })


def crear_proyecto(request):
    form = ProjectModelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_project = form.save()
            return redirect('/proyectos')
    return render(request, 'todo/nuevo_proyecto.html', {
        "form": form,
    })


def buscar(request):
    q = request.POST.get('q')
    tasks = Task.objects.filter(
        Q(title__icontains=q) | Q(desc__icontains=q)
    )
    if q in ['urgente', 'urgentes']:
        tasks = tasks | Task.objects.filter(high_priority=True)
    num_tasks = tasks.count()
    print(f"num_tasks is {num_tasks}")
    return render(request, "todo/buscar.html", {
        'q': q,
        'tasks': tasks,
        'num_tasks': num_tasks,
    })
