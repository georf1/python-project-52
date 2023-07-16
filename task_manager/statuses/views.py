from django.urls import reverse_lazy as _
from django.utils.translation import gettext_lazy
from django.views.generic.list import ListView
from task_manager.statuses.models import Status
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from task_manager.statuses.forms import StatusForm


class StatusesListView(ListView):
    template_name = 'list_status.html'

    def get_queryset(self):
        return Status.objects.all()


class StatusesCreateView(CreateView):
    template_name = 'form.html'
    model = Status
    success_url = _('statuslist')
    form_class = StatusForm
    success_message = "Status was created successfully"
    extra_context = {
        'title': gettext_lazy('Create status'),
        'button_text': gettext_lazy('Create'),
    }


class StatusesUpdateView(UpdateView):
    template_name = 'form.html'
    model = Status
    success_url = _('statuslist')
    form_class = StatusForm
    success_message = "Status was updated successfully"
    extra_context = {
        'title': gettext_lazy('Update status'),
        'button_text': gettext_lazy('Update'),
    }


class StatusesDeleteView(DeleteView):
    template_name = 'delete_status.html'
    model = Status
    success_url = _('statuslist')
    extra_context = {
        'title': gettext_lazy('Delete status'),
        'button_text': gettext_lazy('Yes, delete'),
    }
