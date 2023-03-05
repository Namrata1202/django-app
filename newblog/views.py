from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Blognew
from .models  import Comment
from .forms import BlogForm
from django.contrib.auth import authenticate, login,logout 

# Create your views here.
def register(request):
    if request.method== 'POST':
        uname =request.POST.get('name')
        Fname=request.POST.get('Fname')
        Lname=request.POST.get('Lname')
        uemail =request.POST.get('Eid')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        if pass1!=pass2:
            messages.warning(request,'password does  not match')
            return redirect('register')
        elif  User.objects.filter(username=uname).exists():
            messages.warning(request,'username already taken')
            return redirect('register')
        elif  User.objects.filter(email=uemail).exists():
            messages.warning(request,'email already exists')
            return redirect('register') 
        else:
            userdata= User.objects.create_user(username=uname,password=pass1,email=uemail,first_name=Fname,last_name=Lname)
            userdata.save()
            messages.success(request, 'you has been registered successfully')
            return redirect('login_Page')

        


    return render(request,"newblog/register.html",{})

def home(request):
    blog=Blognew.objects.all()
    
    
   
    return render(request,"newblog/home.html",{'blog':blog})


def login_Page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username,password=password)
        if user is not  None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request,'Invalid credentials')
            return redirect('login_Page')


    
    return render(request,"newblog/login.html",{})

def user_logout(request):
    logout(request)
    return redirect('home')

def post_blog(request):
    if request.method=='POST':
        title=request.POST.get('title')
        des=request.POST.get('des')
        blog=Blognew(title=title,dsc=des,user_id=request.user)
        blog.save()
        messages.success(request,'post has been submitted successfully')
        return redirect('post_blog')





    return render(request,'newblog/blog_post.html',{}) 

def post_detail(request,idd):
    Nblog=Blognew.objects.get(pk=idd)
    msg= False
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            
            if Nblog.likes.filter(id=user.id).exists():
                Nblog.likes.remove(user)
                msg=False
            else:
                    Nblog.likes.add(user)
                    msg=True

                     
    
    return render(request,'newblog/post_detail.html',{'Nblog':Nblog, 'msg':msg})


def post_delete(request,idd):
    blog=Blognew.objects.get(pk=idd)
    blog.delete()
    return redirect('home')


def post_edit(request,idd):
    blog=Blognew.objects.get(pk=idd)
    editblog= BlogForm(instance=blog)
    if request.method == 'POST':
        editblog=BlogForm(request.POST,instance=blog)
        if editblog.is_valid():
            editblog.save()
            return redirect('post_detail',idd=blog.pk)


    return render(request,'newblog/edit.html',{'editblog':editblog})

def like_post(request,idd):
    post=Blognew.objects.filter(pk=idd)
    msg= False
    if request.user.is_authenticated:
            user = request.user
            if post[0].unlikes.filter(id=user.id).exists():
                post[0].unlikes.remove(user)


            if request.user in post[0].likes.all():
                post[0].likes.remove(user)
                msg=False
                    
            else:
                post[0].likes.add(user)
                msg=True

                 

                        

                
           

            
           


    
    return redirect('home')

def unlike_post(request,idd):
    post=Blognew.objects.filter(pk=idd)
    msg= False
    if request.user.is_authenticated:
        user = request.user
        if post[0].likes.filter(id=user.id).exists():
            post[0].likes.remove(user)

        if request.user in post[0].unlikes.all():
            post[0].unlikes.remove(user)
                    
                    

        else:
            post[0].unlikes.add(user)
    return redirect('home')

def comment_post(request,idd):
    blogg=Blognew.objects.get(pk=idd)
    
    
    if request.method=='POST':
        title=request.POST.get('comment')
        blog=Comment(body=title,post_id=idd,usr=request.user)

        
        
            
        
        
        blog.save()
        
        return redirect('post_detail',idd=blogg.pk)

def author_post(request):
    if request.method=='POST':
        aname =request.POST.get('aname')
        fblog=Blognew.objects.filter(title__contains=aname)
        
        print(fblog)
        



                

    return render(request,'newblog/searchtitle.html',{'fblog':fblog})
    


    
    

