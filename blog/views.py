from django.shortcuts import render,redirect,get_object_or_404
from  .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    post=Post.objects.all()
    

    return render(request, 'blog/base.html',{'post':post})


def post_detail(request,idd):
    post=Post.objects.get(pk=idd)
    return render(request,'blog/post_detail.html',{'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            return redirect('post_detail',idd=post.pk)
    else:
        form = PostForm()
    return render(request,'blog/post_edit.html',{'form':form})   

def edit_post(request,idd):
    post = get_object_or_404(Post, pk=idd)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
        
            
            
            post.save()
            return redirect('post_detail', idd=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})     
