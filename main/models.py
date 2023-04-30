from django.db import models
class Articles(models.Model):
    year = models.IntegerField('Год публикации', max_length=1000)
    title=models.TextField('Название статьи',max_length=1000)
    authors = models.TextField('Авторы', max_length=1000)
    url= models.TextField('Ссылка на публикацию', max_length=1000)
    def __str__(self):
        return self.title
# Create your models here.
