import os
import datetime

from django.shortcuts import render

from todo.models import Task, Project


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
