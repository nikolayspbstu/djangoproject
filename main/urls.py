from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('',views.base,name='home'),
    path('about',views.about,name='about'),
    path('personality',views.teacherteam,name='personal'),
    path('admin/',admin.site.urls),

]
