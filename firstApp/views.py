from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  return render(request, "firstapp/index.html")

def jurco(request):
  return HttpResponse('Hello Jurco')

def david(request):
  return HttpResponse('Hello David !!!')

def greet(request, name):
  return render(request, "firstapp/greet.html", {
    "name": name.capitalize()
  })