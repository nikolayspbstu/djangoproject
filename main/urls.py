from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('',views.main_str,name='home'),
    path('about',views.about,name='about'),
    path('personality',views.teacherteam,name='personal'),
    path('admin/',admin.site.urls),
    #path('smirnov',views.publication,name='smirnov'),

]
