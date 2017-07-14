from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login,logout
from .import forms

class LoginView(generic.FormView):
    form_class=AuthenticationForm
    success_url = reverse_lazy("Home")
    template_name = "login.html"

    def get_form(self,form_class=None):
        if form_class is None:
            form_class=self.get_form_class()
        return form_class(self.request,**self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request,form.get_user())
        return super().form_valid(form)

class LogoutView(generic.RedirectView):
    url= reverse_lazy("Home")

    def get(self,request,*args,**kwargs):
        logout(request)
        return super().get(request,*args,**kwargs)

class SignUp(generic.CreateView):
    form_class= forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'signup.html'



