from django import forms
from .models import Image
from .models import Extract


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('Password','Data', 'image1')
    
class ImageExt(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Extract
        fields = ('Password2', 'image2')