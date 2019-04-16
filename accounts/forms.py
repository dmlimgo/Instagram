from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django import forms

class UserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.widget.attrs.update({'placeholder': field.label})
            field.label=''
            field.help_text=''
            
        # self.fields['password1'].label = ''
        # self.fields['password2'].label = ''
        # self.fields['password1'].help_text = ''
        # self.fields['password2'].help_text = ''
        # self.fields['password1'].placeholder = '비밀번호1'
        # self.fields['username'].widget.attrs.update({'placeholder': ''})
        