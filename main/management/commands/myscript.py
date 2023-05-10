from django.core.management.base import BaseCommand
import os
import django
import json
# Указываем путь к файлу настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testsite.settings')

# Инициализируем Django
django.setup()
from main.models import Article, Teacher




class Command(BaseCommand):
    help = 'My custom script'

    def handle(self, *args, **options):
        json_dir = 'main/teachers'
        for filename in os.listdir(json_dir):
            if filename.endswith('.json'):
                with open(os.path.join(json_dir, filename), 'r', encoding='utf-8') as f:
                    json_data = json.load(f)
                Name=filename.title().replace('.Json', '')
                Name=Name.title().rstrip()
                teacher, created = Teacher.objects.get_or_create(name=Name)
                for article_data in json_data:
                    year=article_data['Year']
                    title = article_data['Title']

                    author_name = article_data['Authors']
                    Article.objects.create(title=author_name, content=title,year=year, teacher=teacher)
                print(Name)

