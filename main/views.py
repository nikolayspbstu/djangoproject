from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import admin
from .models import Teacher, Article
from .forms import ArticleFilterForm
from django.http import JsonResponse
import json
from django.http import HttpResponse
# Create your views here.
def load_articles(request):
    form = ArticleFilterForm(request.GET or None)
    articles = []

    if request.GET.get('teacher') and request.GET.get('year'):
        articles = Article.objects.filter(
            teacher__id=request.GET.get('teacher'),
            year=request.GET.get('year')
        )

    return render(request, 'main/load.html', {'form': form, 'articles': articles})


def download_articles(request):
    if request.method == 'GET':
        articles = []

        if request.GET.get('teacher') and request.GET.get('year'):
            articles = Article.objects.filter(
                teacher__id=request.GET.get('teacher'),
                year=request.GET.get('year')
            )

        articles_json = json.dumps([article.to_dict() for article in articles], ensure_ascii=False,indent=4)

        response = HttpResponse(articles_json, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="articles.json"'
        return response


def index(request):

    return render(request,'main/index.html')



def about(request):

    return render(request,'main/about.html')

def kafedr(request):

    return render(request,'main/kafedr.html')

def teacherteam(request):
    text='д.ф.-м.н., профессор, научный руководитель магистерской программы "Модели и высокопроизводительные вычисления в физической гидрогазодинамике"'
    return render(request, 'main/personal.html')



def smirnov(request):
    teacher = Teacher.objects.get(id=17)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def zaytsev(request):
    teacher = Teacher.objects.get(id=7)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def paskevich(request):
    teacher = Teacher.objects.get(id=13)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def strelec(request):
    teacher = Teacher.objects.get(id=21)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def chumakov(request):
    teacher = Teacher.objects.get(id=24)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def abramov(request):
    teacher = Teacher.objects.get(id=1)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def bulovich(request):
    teacher = Teacher.objects.get(id=2)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def galaev(request):
    teacher = Teacher.objects.get(id=3)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def garbaruk(request):
    teacher = Teacher.objects.get(id=4)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def zasimova(request):
    teacher = Teacher.objects.get(id=8)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def ivanov(request):
    teacher = Teacher.objects.get(id=9)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def kitanina(request):
    teacher = Teacher.objects.get(id=7)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def kolesnik(request):
    teacher = Teacher.objects.get(id=10)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def levchenya(request):
    teacher = Teacher.objects.get(id=12)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def pletnev(request):
    teacher = Teacher.objects.get(id=14)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def smirnovskiy(request):
    teacher = Teacher.objects.get(id=18)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def talalov(request):
    teacher = Teacher.objects.get(id=22)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def shur(request):
    teacher = Teacher.objects.get(id=27)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def garaulin(request):
    teacher = Teacher.objects.get(id=5)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def golubkov(request):
    teacher = Teacher.objects.get(id=6)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def sinicina(request):
    teacher = Teacher.objects.get(id=16)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def muhortova(request):
    teacher = Teacher.objects.get(id=17)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def pozilov(request):
    teacher = Teacher.objects.get(id=15)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def telnov(request):
    teacher = Teacher.objects.get(id=23)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def scur(request):
    teacher = Teacher.objects.get(id=28)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def uhnev(request):
    teacher = Teacher.objects.get(id=29)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def ignatieva(request):
    teacher = Teacher.objects.get(id=22)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def koleshko(request):
    teacher = Teacher.objects.get(id=11)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def snegirev(request):
    teacher = Teacher.objects.get(id=19)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def stepanov(request):
    teacher = Teacher.objects.get(id=20)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)

def shmidt(request):
    teacher = Teacher.objects.get(id=25)
    articles = teacher.articles.all()
    context = {'teacher': teacher, 'articles': articles}
    return render(request, 'main/publications/teach_shablon.html',context)


def admin(request):

    return render(request,'main/admin.html')


