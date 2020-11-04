from django import forms
from . import models

class ProjectForm(forms.Form):
    id_project = forms.CharField(max_length=3)
    name = forms.CharField(max_length=64)
    about = forms.CharField(widget=forms.Textarea, required=False)



class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = models.Project
        exclude = ['about',]