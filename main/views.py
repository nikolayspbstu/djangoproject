from django.shortcuts import render
from parser import collect,lower_func
from .models import Articles
# Create your views here.

def about(request):

    return render(request,'main/about.html')

def teacherteam(request):
    natural = list(range(1,2))
    dict_list = collect()
    text='д.ф.-м.н., профессор, научный руководитель магистерской программы "Модели и высокопроизводительные вычисления в физической гидрогазодинамике"'
    return render(request, 'main/personal.html', {'data': dict_list,'natural':natural})
def base(request):
    all = Articles.objects.all()
    return render(request,'main/index.html',{'all':all})
