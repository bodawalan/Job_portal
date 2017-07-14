from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Suggestion
from .forms import Sugesstion_Form
from django.core.urlresolvers import reverse
from .import forms
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin

def Suggestion_View(request):
    form=forms.Sugesstion_Form()
    if request.method == "POST":
        form = forms.Sugesstion_Form(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            return HttpResponseRedirect(reverse('fillform'))
    return render(request,'sugesstion.html',{'suggestion':form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('fillform')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def Home(request):
    return render(request,'Home.html',)