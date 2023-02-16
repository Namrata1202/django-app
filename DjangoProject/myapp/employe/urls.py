from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("add/",Employe_home),
    path("allemploye/",All_Employe),
    path("delete_emp/<int:idd>",delete_emp),
    path("update_emp/<int:idd>",update_emp),
    path("doupdate_emp/<int:idd>",doupdate_emp)

    
]
