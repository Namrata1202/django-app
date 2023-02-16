from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employe
# Create your views here.


def  All_Employe(request):
    emps=Employe.objects.all()
    return render(request,"about.html",{'emps':emps})

def Employe_home(request):
    if request.method=="POST":
        #data fetch
        emp_name=request.POST.get("Ename")
        emp_idd=request.POST.get("Eid")
        emp_phone=request.POST.get("Enumber")
        emp_address=request.POST.get("Eaddress")
        emp_working=request.POST.get("Eworking")
        

        e=Employe()
        e.name=emp_name
        e.emp_id=emp_idd
        e.phone=emp_phone
        e.address=emp_address
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()
        

        
    return render(request,"Add.html")


def delete_emp(request,idd):
    emp=Employe.objects.get(pk=idd)
    emp.delete()
    return redirect("/employe/allemploye")

def update_emp(request,idd):
    emp=Employe.objects.get(pk=idd)
    return render(request,"update_emp.html",{'emp':emp})


def doupdate_emp(request,idd):
    if request.method=="POST":
        #data fetch
        emp_name=request.POST.get("Ename")
        emp_idd=request.POST.get("Eid")
        emp_phone=request.POST.get("Enumber")
        emp_address=request.POST.get("Eaddress")
        emp_working=request.POST.get("Eworking")

        e=Employe.objects.get(pk=idd)
        

        
        e.name=emp_name
        e.emp_id=emp_idd
        e.phone=emp_phone
        e.address=emp_address
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        e.save()

    return redirect("/employe/allemploye")   
