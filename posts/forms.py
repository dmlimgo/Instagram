from .models import Post, Image
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content',)
        widgets = {
                    'content': forms.Textarea(attrs={'placeholder': '내용을 입력하세요'})
                    }
        labels = {
                    'content': '내용'
                    }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('file',)
        widgets = {
            'file': forms.FileInput(attrs={'multiple':True}),
        }