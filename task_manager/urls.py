from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from task_manager.views import UserLoginView
from task_manager.views import UserLogoutView


urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('users/', include('task_manager.users.urls')),
    path('admin/', admin.site.urls),
]
