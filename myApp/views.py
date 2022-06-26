from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    countries = Viloyatlar.objects.all()
    return render(request,'index.html',{"countries":countries})

def load_post(request):
    t_id = request.GET['selectregion']
    malumot = Tashkilotlar.objects.get(id=t_id)
    return render(request,'post.html',{"malumot":malumot})

def load_zone(request):
    region_id = request.GET['country']
    cities = IqtisodiyZonalar.objects.filter(region_id=region_id).order_by('name')
    return render(request,'load_zone.html',{"cities":cities})


def load_org(request):
    region_id = request.GET['tashkilot']
    cities = Tashkilotlar.objects.filter(i_zona=region_id)
    return render(request,'load_org.html',{"cities":cities})



def static(request):
    return render(request,'static.html')


def error_404(request,exception):
    return render(request,'error_404.html')