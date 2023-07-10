from django import forms
from .models import RoomReview


class RoomReviewForm(forms.ModelForm):
    class Meta:
        model = RoomReview
        fields = ('name', 'email', 'image', 'message', 'mark', 'room')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your name'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your email'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your image'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Start the discussion...'
        })


