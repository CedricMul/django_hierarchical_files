from django import forms
from file_app.models import File
from mptt.forms import TreeNodeChoiceField


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['isFile', 'parent', 'name']