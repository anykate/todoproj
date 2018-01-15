from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.decorators.http import require_POST
from .models import ToDo
from .forms import ToDoForm


# Create your views here.
def index(request):
    form = ToDoForm()
    todos = ToDo.objects.order_by('-created_at')
    return render(request, 'todo/index.html', {'todos': todos, 'form': form})


@require_POST
def addToDo(request):
    form = ToDoForm(request.POST)

    if form.is_valid():
        new_todo = ToDo(text=request.POST['text'])
        new_todo.save()

    return HttpResponseRedirect('/')


def completeToDo(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.complete = True
    todo.save()
    return HttpResponseRedirect('/')


def deleteCompleted(request):
    ToDo.objects.filter(complete__exact=True).delete()
    return HttpResponseRedirect('/')


def deleteAll(request):
    ToDo.objects.all().delete()
    return HttpResponseRedirect('/')
