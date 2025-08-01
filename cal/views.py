from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return HttpResponse("Welcome to the Calculator App!")
def index(request):
    return render(request, 'index.html')