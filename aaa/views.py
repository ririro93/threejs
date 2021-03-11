from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def line(request):
    return render(request, 'line.html')