from django.shortcuts import render,redirect
from . import forms
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.utils.decorators import method_decorator
# Create your views here.

def show(request):
    if request.method == "POST":
        postform = forms.MusicianForm(request.POST)
        if postform.is_valid():
            postform.save()
            return redirect('show')
    else:
        postform = forms.MusicianForm()
    return render(request, 'show.html',{'form':postform})

@method_decorator(login_required,name=('dispatch'))
class Edit_musician(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    pk_url_kwarg ='id'
    success_url = reverse_lazy('show')
    template_name ='show.html'