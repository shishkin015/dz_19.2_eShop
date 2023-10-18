import json
import os

from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    """
    Команда удаляет данные из БД и заполняет БД из .json файла

    Реализовано два способа:
    1. Удаляет данные вместе с ID и вносит данные вновь из .json файла
    2. Распаковывает .json файл и записывает фикстуры с последующими ID
    """
    def handle(self, *args, **options):
        # 1. Способ:
        Category.objects.all().delete()
        return os.system("python manage.py loaddata catalog.json")

        # 2. Способ:
        # with open('catalog.json', 'rb') as f:
        #     data = json.load(f)
        #
        #     category_for_data = []
        #     for i in data:
        #         print(i['fields'])
        #         category_for_data.append(
        #             Category(**i['fields'])
        #         )
        #     Category.objects.bulk_create(category_for_data)

