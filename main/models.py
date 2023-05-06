from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=300)
    # Добавьте другие поля, если нужно

    def __str__(self):
        return self.name



class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()


    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


    def __str__(self):
        return self.title