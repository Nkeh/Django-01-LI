from django import forms

from . import models

class NoteForm(forms.ModelForm):
    class Meta: 
        model = models.Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-5'}),

        }