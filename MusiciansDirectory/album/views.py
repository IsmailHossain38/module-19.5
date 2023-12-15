from django.shortcuts import render,redirect
from . import forms
from . import models
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.auth.forms  import AuthenticationForm 
from django.contrib.auth.views import LoginView
from django.contrib.auth  import authenticate ,login,logout 
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView ,UpdateView ,DeleteView
from django.utils.decorators import method_decorator
from django.contrib import messages
# Create your views here.

@method_decorator(login_required,name=('dispatch'))
class Index(CreateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name ='index.html'
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        return super().form_valid(form)
    

@method_decorator(login_required,name=('dispatch'))
class Edit_album(UpdateView):
    model = models.AlbumModel
    form_class = forms.AlbumForm
    template_name ='index.html'
    pk_url_kwarg = 'id'
    success_url =reverse_lazy('homepage')



@method_decorator(login_required,name=('dispatch'))
class Delete_model(DeleteView):
    model =models.AlbumModel
    template_name= 'delete_view.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
    


def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form':form})
        

class User_login(LoginView):
    template_name = 'register.html'
    def form_valid(self, form):
        messages.success(self.request ,'logged in successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request ,'logged information incorrect')
        return super().form_invalid(form)
    def get_success_url(self) -> str:
        return reverse_lazy('homepage')
 

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')