from django.urls import path
from . import views

urlpatterns = [
    path('newBlog/', views.register,name='register'),
    path('home/',views.home, name='home'),
    path('login/',views.login_Page,name='login_Page'),
    path('logout/',views.user_logout,name='user_logout'),
    path('post_blog/',views.post_blog,name='post_blog'),
    path('post_detail/<int:idd>',views.post_detail,name='post_detail'),
    path('post_delete/<int:idd>',views.post_delete,name='post_delete'),
    path('post_edit/<int:idd>',views.post_edit,name='post_edit'),
    path('likes/<int:idd>/',views.like_post,name='like'),
    path('unlikes/<int:idd>/',views.unlike_post,name='unlike'),
    path('comments/<int:idd>/',views.comment_post,name='comments'),
    path('author/',views.author_post,name='author')

    
    

]