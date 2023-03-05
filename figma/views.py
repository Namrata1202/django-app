from django.shortcuts import render
from .models import Country
from .models import Clients


# Create your views here.
def home(request):
    country = Country.objects.all().order_by('-id')[:6]
    scountry = Country.objects.all().order_by('-id')[:3]
    client = Clients.objects.all()
    print(country) 
    

    return render(request,"main.html",{'country':country, 'scountry':scountry, 'client':client})

def booking(request):
    return render(request,"booking.html")  

def gallery(request):
    print("entered here")
    print("new")
    return render(request,"Gallery.html")      

