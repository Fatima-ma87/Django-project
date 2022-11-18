from django import forms
from django.core.files.images import get_image_dimensions
from django.db.models import fields
from core_objects.models import * 
from core_objects.forms import *


class ResizingForm(forms.ModelForm):
    
    class Meta:
        widgets = { 
            'headline': forms.Textarea(attrs={
                'placeholder':'max. 40 characters',
                'rows':2,
                'cols':40}),
            'bodyText': forms.Textarea(attrs={
                'placeholder':'max. 450 characters',
                'rows':8,
                'cols':75}),           
        }
