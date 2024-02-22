from django.shortcuts import render
from . import models
from django.template import loader
from django.http import HttpResponse



def show(request):
    youna=models.Product.objects.all()
    arg={"myvar":youna}
    return render(request,'index.html',arg)


def show1(request):
    # youna=models.Product.objects.all()
    # arg={"myvar":youna}
    return render(request,'aboutUS.html')
