from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('blog', 'name', 'image', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your name'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your image'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'enter your message...'
        })
