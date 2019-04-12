from .models import Post
from django.forms import ModelForm, TextInput, Textarea
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('content',)
        # widgets = {
        #             'content': Textarea(attrs={'placeholder': '내용을 입력하세요'})
        #             }
        # def __init__(self, *args, **kwargs):
        #     super(PostForm, self).__init__(*args, **kwargs)
        #     self.helper = FormHelper()
