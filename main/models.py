from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=300)
    # Добавьте другие поля, если нужно

    def __str__(self):
        return self.name



class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    year=models.IntegerField(null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='articles')


    def __str__(self):
        return self.title