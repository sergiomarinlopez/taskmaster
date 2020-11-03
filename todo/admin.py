from django.contrib import admin

from todo.models import Task, Project, Document

class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'id_task',
        'project_id',
        'size',
        'high_priority',
        'is_due',
    )
    list_filter = ('high_priority', 'size')
    search_fields = ('title', 'desc')
    date_hierarchy = 'created'

admin.site.register(Task, TaskAdmin)


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)



class DocumentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Document, DocumentAdmin)
