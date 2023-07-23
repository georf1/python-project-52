from django.urls import reverse_lazy as _
from django.utils.translation import gettext_lazy
from django_filters.views import FilterView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm
from django.contrib.auth.models import User
from task_manager.tasks.filters import TaskFilter


class TasksListView(FilterView):
    template_name = 'list_task.html'
    model = Task
    filterset_class = TaskFilter
    context_object_name = 'tasks'
    extra_context = {
        'title': gettext_lazy('Tasks'),
        'button_text': gettext_lazy('Show'),
    }



class TaskDetailView(DetailView):
    template_name = 'task.html'
    model = Task
    context_object_name = 'task'
    extra_context = {
        'title': gettext_lazy('Task preview')
    }


class TaskCreateView(CreateView):
    template_name = 'form.html'
    model = Task
    success_url = _('tasks_list')
    form_class = TaskForm
    success_message = "Task was created successfully"
    extra_context = {
        'title': gettext_lazy('Create task'),
        'button_text': gettext_lazy('Create'),
    }

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    template_name = 'form.html'
    model = Task
    success_url = _('tasks_list')
    form_class = TaskForm
    success_message = "Task was updated successfully"
    extra_context = {
        'title': gettext_lazy('Update task'),
        'button_text': gettext_lazy('Update'),
    }


class TaskDeleteView(DeleteView):
    template_name = 'delete_task.html'
    model = Task
    success_url = _('tasks_list')
    extra_context = {
        'title': gettext_lazy('Delete Task'),
        'button_text': gettext_lazy('Yes, delete'),
    }
