from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'note']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'input-title',
                'placeholder': 'Введите заголовок'
            }),
            'note': forms.Textarea(attrs={
                'class': 'input-note',
                'placeholder': 'Введите заметку',
                'rows': 5
            })
        }

