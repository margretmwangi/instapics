from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .models import post , Like
from django.contrib import messages
from.forms import UserRegisterForm
from django.views.generic import(
    ListView,
    CreateView

)
# Create your views here.

def index(request):
    return render(request, 'insta/index.html')
   
class PostListView(ListView):
    template_name = "insta/post.html"
    queryset = post.objects.all()
    context_object_name = 'posts'

class PostCreateView(CreateView):
    template_name = 'insta/create.html'
    form_class = PostForm
    queryset = post.objects.all()
    success_url = 'post/'
    def form_invalid(self,form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)
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

def like_post(request):
    return redirect('posts:post')