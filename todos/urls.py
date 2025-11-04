from django.urls import path

from .views import home_view,tasks_view,add_task_view

app_name = 'todos'


urlpatterns = [
    path('',home_view,name='home_page'),
    path('tasks/',tasks_view,name='tasks_page'),
    path('add/',add_task_view,name='add_page'),
]
