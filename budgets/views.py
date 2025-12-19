from django.shortcuts import render, HttpResponse

# Create your views here.
def hello_world_view(request):
    return HttpResponse('Hello World! Welcome to my budgeting app!')