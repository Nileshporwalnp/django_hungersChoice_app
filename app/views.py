from django.shortcuts import render
from .models import FastFood,Chinese
# Create your views here.
def index(request):
    context={'active_link':'index'}
    return render(request,'app/index.html',context)

def fastfood(request):
    fastfoods=FastFood.objects.all()
    context={
        'fastfoods':fastfoods,
        'active_link':'fastfood'
    }
    return render(request,'app/fastfood.html',context)

def chinese(request):
    chinese=Chinese.objects.all()
    context={
        'chinese':chinese,
        'active_link':'chinese'
    }
    return render(request,'app/chinese.html',context)