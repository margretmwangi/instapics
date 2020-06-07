from django.shortcuts import render, redirect
from .models import post
from django.contrib import messages
from.forms import UserRegisterForm
from django.views.generic import(
    ListView,

)
# Create your views here.

def index(request):
    return render(request, 'insta/index.html')
   
class PostListView(ListView):
    template_name = "insta/post.html"
    queryset = post.objects.all()
    context_object_name = 'posts'

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}')
            return redirect('post/')
    else :

        form = UserRegisterForm()
    return render(request,'registration/register.html' , {'form':form})

def login(request):

    return render(request, 'registration/login.html') 
    


  