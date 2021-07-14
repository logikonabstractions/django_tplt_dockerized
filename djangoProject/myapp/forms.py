from django import forms
from .models import ImageModel

class UploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ('file',)

