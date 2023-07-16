from django.urls import path
from task_manager.tasks.views import TasksListView
from task_manager.tasks.views import TaskDetailView
from task_manager.tasks.views import TaskCreateView
from task_manager.tasks.views import TaskUpdateView
from task_manager.tasks.views import TaskDeleteView

urlpatterns = [
    path('', TasksListView.as_view(), name='tasks_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/', TaskDetailView.as_view()),
    path('<int:pk>/update/', TaskUpdateView.as_view()),
    path('<int:pk>/delete/', TaskDeleteView.as_view()),
]
