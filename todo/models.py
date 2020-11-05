from django.db import models
from django.core.exceptions import ValidationError

import arrow

# Create your models here.


class Project(models.Model):
    id_project = models.SlugField(max_length=12, primary_key=True)
    name = models.CharField(max_length=64)
    about = models.TextField(
        verbose_name="Acerca de...",
        blank=True,
        help_text="(No es obligatorio)",
        )
    started = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id_project}: {self.name}"


class Task(models.Model):
    id_task = models.AutoField(primary_key=True)
    project = models.ForeignKey(
        Project, 
        on_delete=models.PROTECT,
        default='DEF',
        )
    title = models.CharField(max_length=220)
    desc = models.TextField(
        blank=True,
        help_text="(No es obligatorio)",
        )
    size = models.IntegerField(
        help_text="5 posibles tamaños",
        verbose_name='Tamaño de la tarea',
        choices=[
            (1, 'Trivial'),
            (2, 'Pequeña'),
            (3, 'Normal'),
            (4, 'Grande'),
            (5, 'Muy Grande'),
        ],
        default=3,
        )
    high_priority = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    closed = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.project_id}-{self.id_task}: {self.title}"

    def is_due(self):
        if self.closed:
            return False
        time_now = arrow.utcnow()
        ref_time = time_now.shift(days=-7)
        if self.created < ref_time:
            return True
        else:
            return False

    def is_closed(self):
        self.closed != None
    

class Document(models.Model):
    id_document = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    document_name = models.CharField(max_length=200)
    archive = models.FileField(upload_to='task/docs')

    def __str__(self):
        return self.document_name














