from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request,'main/index.html')



def about(request):

    return render(request,'main/about.html')

def teacherteam(request):
    text='д.ф.-м.н., профессор, научный руководитель магистерской программы "Модели и высокопроизводительные вычисления в физической гидрогазодинамике"'
    return render(request, 'main/personal.html')


def smirnov(request):
    return render(request, 'main/publications/smirnov.html')