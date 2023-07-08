from django.urls import path
from task_manager.users.views import UsersListView
from task_manager.users.views import SignUpView
from task_manager.users.views import UserUpdateView
from task_manager.users.views import UserDeleteView


urlpatterns = [
    path('', UsersListView.as_view(), name='userlist'),
    path('create/', SignUpView.as_view(), name='create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete')
]
