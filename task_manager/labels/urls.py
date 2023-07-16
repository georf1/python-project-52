from django.urls import path
from task_manager.labels.views import LabelsListView
from task_manager.labels.views import LabelsCreateView
from task_manager.labels.views import LabelsUpdateView
from task_manager.labels.views import LabelsDeleteView


urlpatterns = [
    path('', LabelsListView.as_view(), name='labels_list'),
    path('create/', LabelsCreateView.as_view(), name='create_label'),
    path('<int:pk>/update/', LabelsUpdateView.as_view()),
    path('<int:pk>/delete/', LabelsDeleteView.as_view())
]
