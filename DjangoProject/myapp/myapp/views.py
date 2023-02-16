from django.http import HttpResponse
from django.shortcuts import render
def home(request):

    if request.method=='POST':
        myformdata= request.POST['ndata']
        print(myformdata)
    print("this is new project")
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")    