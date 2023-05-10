import datetime
from django import forms
from .models import Teacher

YEAR_CHOICES = [(str(year), str(year)) for year in range(2000, datetime.date.today().year+1)]

class ArticleFilterForm(forms.Form):
    teacher = forms.ModelChoiceField(queryset=Teacher.objects.all())
    year = forms.ChoiceField(choices=YEAR_CHOICES)
    fields = ['teacher', 'year']