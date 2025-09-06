from django.forms import ModelForm,widgets
from .models import Project
from django import forms
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # note id, created from projects will not be there .
        # since id not editible and created is automatically generated.
        fields = ['title', 'featured_image','description','demo_link','source_link','tags']

        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

        def __init__(self,*args, **kwargs):
            super(ProjectForm,self).__init__(*args,**kwargs)
            # self.fields['title'].widget.attrs.update({
            #     'class':'input',
                
                # })
            for name,field in self.fields.items():
                field.widget.attrs.update({'class':'input'})