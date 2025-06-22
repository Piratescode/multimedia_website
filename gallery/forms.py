from django import forms
from .models import MediaFile

class MediaFileForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['title', 'media_type', 'file']