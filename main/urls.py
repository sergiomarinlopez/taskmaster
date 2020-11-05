import datetime
import os

from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.urls import include

import debug_toolbar

import todo.views

urlpatterns = [
    path('', todo.views.homepage, name="homepage"),
    path('tareas/', todo.views.tareas),
    path(
        'tareas/<int:id_tarea>',
        todo.views.detalle_tarea,
        name="detail_task",
        ),
    path('proyectos/', todo.views.proyectos),
    path('proyectos/nuevo/', todo.views.crear_proyecto),
    path('hola/', todo.views.hola),
    path('files/', todo.views.files),
    path('hola/<int:num>', todo.views.numero),
    path('buscar', todo.views.buscar),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns.append(
        re_path(
            r'^media/(?P<path>.*)$', serve, {
                'document_root': settings.MEDIA_ROOT,
            }),
        )
    urlpatterns.append(
        re_path(
            r'^static/(?P<path>.*)$', serve, {
                'document_root': settings.STATIC_ROOT,
            }),
        )
