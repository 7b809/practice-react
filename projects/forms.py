from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # note id, created from projects will not be there .
        # since id not editible and created is automatically generated.
        fields = ['title','description','demo_link','source_link','tags']