from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello there, store coming soon...")

def details(request):
    return HttpResponse("Some details go here")