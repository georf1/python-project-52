from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy as _
from django.utils.translation import gettext_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('This is index view')


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'form.html'
    form_class = AuthenticationForm
    next_page = _('home')
    success_message = "You are logged in"
    extra_context = {
        'title': gettext_lazy('Login'),
        'button_text': gettext_lazy('Enter'),
    }


class UserLogoutView(LogoutView):
    next_page = _('home')
    success_message = "You are logged out"
