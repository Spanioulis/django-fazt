from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Person, Task
from .forms import CreateNewTask

# Create your views here.

def index(request):
  title = 'Welcome to Django Fazt!!'
  return render(request, 'index.html', {
    "title": title
  })

def hello(request, username):
  return HttpResponse("<h1>Hola %s!</h1>" % username)

def about(request):
  username = 'Spanioulis'
  return render(request, 'about.html', {
    "username": username
  })

def persons(request):
  # persons = list(Person.objects.values())
  # return JsonResponse(persons, safe=False)
  persons = Person.objects.all( )

  return render(request, 'persons/persons.html', {
    "persons": persons,
  })

def tasks(request):
  # task = get_object_or_404(Task, id=id)
  # return HttpResponse('task: %s' % task.title)
  tasks = Task.objects.all()
  return render(request, 'tasks/tasks.html', {
    'tasks': tasks,
  })

def create_task(request):
  if request.method == 'GET':
    return render(request, 'tasks/create_task.html', {
      'form': CreateNewTask()
    })
  else:
    Task.objects.create(title=request.POST['title'], description=request.POST['description'], person_id=1)
    return redirect('tasks')
