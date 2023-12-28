from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    # return HttpResponse("Hello Welocome To Main Page")
    return render(request,"main.html")

def domain(request):
    return HttpResponse("Hello Welocome To Domain Page")