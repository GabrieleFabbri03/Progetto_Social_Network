from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['testo']
        widgets = {
            'testo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'A cosa stai pensando?',
                'rows': 3,
                'minlength': 5
            }),
        }