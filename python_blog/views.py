from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request, name):
    string: str = f'Привет {name}'
    return HttpResponse(string)