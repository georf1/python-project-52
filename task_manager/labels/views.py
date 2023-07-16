from django.urls import reverse_lazy as _
from django.utils.translation import gettext_lazy
from task_manager.labels.models import Label
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from task_manager.labels.forms import LabelForm


class LabelsListView(ListView):
    template_name = 'list_label.html'

    def get_queryset(self):
        return Label.objects.all()


class LabelsCreateView(CreateView):
    template_name = 'form.html'
    model = Label
    success_url = _('labels_list')
    form_class = LabelForm
    success_message = "Label was created successfully"
    extra_context = {
        'title': gettext_lazy('Create label'),
        'button_text': gettext_lazy('Create'),
    }


class LabelsUpdateView(UpdateView):
    template_name = 'form.html'
    model = Label
    success_url = _('labels_list')
    form_class = LabelForm
    success_message = "Label was updated successfully"
    extra_context = {
        'title': gettext_lazy('Update label'),
        'button_text': gettext_lazy('Update'),
    }


class LabelsDeleteView(DeleteView):
    template_name = 'delete_label.html'
    model = Label
    success_url = _('labels_list')
    extra_context = {
        'title': gettext_lazy('Delete label'),
        'button_text': gettext_lazy('Yes, delete'),
    }
