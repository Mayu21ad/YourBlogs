from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>WELCOME, POST YOUR THOUGHTS AND CHECK ON FEEDS</h1>")

def about(request):
    return HttpResponse("<h3>About the blog page</h3>")
