from django.shortcuts import render, redirect
from django.http import HttpResponse
def home(request):
    print("jump here")
    return render(request,'index.html')

# def contact(request):
#     print("jump here")
#     return

