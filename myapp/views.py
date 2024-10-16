from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Person, Task

# Create your views here.

def index(request):
  return render(request, 'index.html')

def hello(request, username):
  return HttpResponse("<h1>Hola %s!</h1>" % username)

def about(request):
  return render(request, 'about.html')

def persons(request):
  # persons = list(Person.objects.values())
  # return JsonResponse(persons, safe=False)
  return render(request, 'persons.html')

def tasks(request, id):
  # task = get_object_or_404(Task, id=id)
  # return HttpResponse('task: %s' % task.title)
  return render(request, 'tasks.html')