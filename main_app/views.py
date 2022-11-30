from django.shortcuts import render
from django.http import HttpResponse

# temp add cats class
class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

    def __str__(self):
        return f"{self.name}"

cats = [
    Cat('Rufus', 'tabbycat', 'crazy cat', 103),
    Cat('Simba', 'lion', 'brave', 5),
    Cat('Garfield', 'tabbycat', 'likes lasagna', 43),
]        


# Create (your views here.
def index(request):
    return HttpResponse(request, 'index.html',{'cats':cats})

def about(request):
    return HttpResponse(request, 'about.html')

def contact(request):
    return HttpResponse(request, 'contact.html')

# def blog(request):
#     return HttpResponse('blog')
      
