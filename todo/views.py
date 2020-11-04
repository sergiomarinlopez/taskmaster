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
        "tareas": Task.objects.all(),
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
    from django.http import HttpResponse
    if request.method == 'GET':
        return render(request, 'todo/nuevo_proyecto.html')
    else:
        return HttpResponse(f"""
        Vaya, ha hecho un POST:
        <ul>
        <li>project_id: {request.POST['id_project']}</li>
        <li>name: {request.POST['name']}</li>
        <li>about: {request.POST['about']}</li>
        """)



def crear_proyecto2(request):
    from django.http import HttpResponse
    if request.method == 'GET':
        return render(request, 'todo/nuevo_proyecto.html')
    else:
        id_project = request.POST['id_project']
        name = request.POST['name']
        about = request.POST['about']
        if id_project and name:
            new_project = Project(
                id_project=id_project,
                name=name,
                about=about,
            )
        new_project.save()
        return HttpResponse(f"""
        Vaya, ha hecho un POST:
        Se ha creado el projecto {new_project.pk}
        """)





def crear_proyecto3(request):
    from django.http import HttpResponse
    from todo.forms import ProjectForm

    if request.method == 'GET':
        form = ProjectForm()
        return render(request, 'todo/nuevo_proyecto3.html', {
            "form": form,
        })
    else:
        form = ProjectForm(request.POST)
        if form.is_valid():
            id_project = form.cleaned_data['id_project']
            name = form.cleaned_data['name']
            about = form.cleaned_data['about']
            new_project = Project(
                id_project=id_project,
                name=name,
                about=about,
            )
            new_project.save()
            return HttpResponse(f"""
        Vaya, ha hecho un POST:
        Se ha creado el projecto {new_project.pk}
        """)
        else:
            return render(request, 'todo/nuevo_proyecto3.html', {
                "form": form,
            })



def crear_proyecto3(request):
    from django.shortcuts import redirect
    from todo.forms import ProjectForm
    
    form = ProjectForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            id_project = form.cleaned_data['id_project']
            name = form.cleaned_data['name']
            about = form.cleaned_data['about']
            new_project = Project(
                id_project=id_project,
                name=name,
                about=about,
            )
            new_project.save()
            return redirect('/proyectos')
    return render(request, 'todo/nuevo_proyecto3.html', {
        "form": form,
    })


def crear_proyecto4(request):
    from django.shortcuts import redirect
    from todo.forms import ProjectModelForm
    
    form = ProjectModelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            new_project = form.save()
            return redirect('/proyectos')
    return render(request, 'todo/nuevo_proyecto3.html', {
        "form": form,
    })
