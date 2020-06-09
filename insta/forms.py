from django import forms
from .models import *
from crispy_forms.layout import Layout, Field,  Submit
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('post', 'post' , css_class='btn-primary'))
    class Meta:
        model = post
        fields = ['image', 
        'caption']
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
