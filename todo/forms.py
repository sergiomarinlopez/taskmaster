from django import forms
from . import models


class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = models.Project
        exclude = []

    def clean_id_project(self):
        id_project = self.cleaned_data['id_project']
        if len(id_project) < 3:
            raise forms.ValidationError(
                "Los códigos de proyecto tiene que"
                " tener al menos tres letras"
                )
        return id_project.upper()