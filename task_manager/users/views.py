from django.urls import reverse_lazy as _
from django.utils.translation import gettext_lazy
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.users.forms import UserRegisterForm
from task_manager.users.forms import UserUpdateForm


class UsersListView(ListView):
    template_name = 'userlist.html'
    login_url = '/login/'
    redirect_field_name = 'user_list'

    def get_queryset(self):
        return User.objects.all()


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    success_url = _('login')
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"
    extra_context = {
        'title': gettext_lazy('Create user'),
        'button_text': gettext_lazy('Register'),
    }


class UserUpdateView(UpdateView):
    template_name = 'form.html'
    success_url = _('userlist')
    form_class = UserUpdateForm
    extra_context = {
        'title': gettext_lazy('Update user'),
        'button_text': gettext_lazy('Update'),
    }

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class UserDeleteView(DeleteView):
    template_name = 'delete_user.html'
    success_url = _('userlist')
    extra_context = {
        'title': gettext_lazy('Users'),
    }

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)