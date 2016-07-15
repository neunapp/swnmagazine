# -*- encoding: utf-8 -*-
from django.shortcuts import redirect
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Autentificacion de usuario
from django.contrib.auth import authenticate, login, logout

from .models import User
from .forms import LoginForm, UserForm


class LogIn(FormView):
    '''
    Logeo del usuario
    '''
    template_name = 'users/login/login.html'
    success_url = reverse_lazy('users_app:home-almacen')
    form_class = LoginForm

    def form_valid(self, form):
        # Verfiamos si el usuario y contrasenha son correctos.
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )

        if user is not None:
            if user.is_active and user.type_user == '1':
                login(self.request, user)
                return HttpResponseRedirect(
                    reverse(
                        'users_app:home-almacen'
                    )
                )
            elif user.is_active:
                # si el usuario es activo ira dahboard
                login(self.request, user)
                return super(LogIn, self).form_valid(form)
            else:
                return HttpResponseRedirect(
                    reverse(
                        'users_app:login'
                    )
                )


class LogoutView(View):
    """
    cerrar sesion
    """
    url = '/auth/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:login'
            )
        )

class HomeTemplateView(TemplateView):
    template_name = 'base/dashboardAlmacen.html'
