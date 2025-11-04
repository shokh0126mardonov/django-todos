from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpRequest,HttpResponse

todos = []


def home_view(request:HttpRequest)->HttpResponse:
    return render(
        request=request,
        template_name='home.html'
    )


def tasks_view(request:HttpRequest)->HttpResponse:
    return render(
        request=request,
        template_name='tasks.html',
        context={
            'todos':todos
            }
    )

def add_task_view(request:HttpRequest)->HttpResponse:
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        new_todo = {
            'title':title,
            'description':description
        }
        todos.append(new_todo)
        print(todos)
        return redirect(reverse('todos:tasks_page'))
    else:
        return render(
        request=request,
        template_name='add_task.html',
    )