from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.contrib.auth.views import LoginView, PasswordChangeView
from .forms import LoginForm
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    form_class = LoginForm

    template_name = 'accounts/login.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        login(self.request, form.get_user())
        if remember_me:
            self.request.session.set_expiry(1209600)
        return super(LoginView, self).form_valid(form)

class CustomLogOutView(View):
    def get(self, request):
        logout(request)
        return redirect("home:main-page")
