from django.shortcuts import render
from django.http import HttpResponse

# Create (your views here.
def index(request):
    return HttpResponse('index.html')

def about(request):
    return HttpResponse('about.html')

def contact(request):
    return HttpResponse('contact.html')

# def blog(request):
#     return HttpResponse('blog')
      
