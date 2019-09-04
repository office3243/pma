from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import RegisterForm
from django.contrib.auth import login


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "accounts/register.html"

    def form_valid(self, form):
        new_user = form.save()
        login(self.request, new_user)
        return redirect("portal:home")

