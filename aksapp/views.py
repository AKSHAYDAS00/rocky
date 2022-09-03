from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def athena(request):
    return HttpResponse("python fullstack")
def car(request):
    return HttpResponse("good morning")
def ambu(request):
    return render(request,'submit.html')


# Create your views here.
