from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request,"index.html")

def scop(request):
    return render(request,"scop.html")

def physiotheraphy(request):
    return render(request,"physiotheraphy.html")

def ahs(request):
    return render(request,"ahs.html")

def ot(request):
    return render(request,"ot.html")

def controlcare(request):
    return render(request,"controlcare.html")

