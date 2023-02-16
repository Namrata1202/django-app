from django import forms

from .models import Blognew

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blognew
        fields = ('title', 'dsc',)