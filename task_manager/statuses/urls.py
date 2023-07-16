from django.urls import path
from task_manager.statuses.views import StatusesListView
from task_manager.statuses.views import StatusesCreateView
from task_manager.statuses.views import StatusesUpdateView
from task_manager.statuses.views import StatusesDeleteView


urlpatterns = [
    path('', StatusesListView.as_view(), name='statuslist'),
    path('create/', StatusesCreateView.as_view(), name='create_status'),
    path('<int:pk>/update/', StatusesUpdateView.as_view()),
    path('<int:pk>/delete/', StatusesDeleteView.as_view())
]
