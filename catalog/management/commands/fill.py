
from django.core.management import BaseCommand, call_command
from django.db import IntegrityError, ProgrammingError
from catalog.models import Product, Category


class Command(BaseCommand):
    requires_migrations_checks = True

    def handle(self, *args, **options):
        try:
            product_list = [
                {
                    "pk": 1,
                    "name": "Apple",
                    "description": "Смартфон",
                    "image": "",
                    "category": "гаджет",
                    "purchase_price": 100000,
                    "date_of_creation": "2023-09-30T17:27:14Z",
                    "last_modified_date": "2023-09-30T17:27:19Z"
                },
                {
                    "pk": 2,
                    "name": "Makita",
                    "description": "Болгарка",
                    "image": "",
                    "category": "Электроинструмент",
                    "purchase_price": 10000,
                    "date_of_creation": "2023-09-30T17:45:02Z",
                    "last_modified_date": "2023-09-30T17:45:04Z"
                },
                {
                    "pk": 3,
                    "name": "JBL",
                    "description": "Колонка",
                    "image": "",
                    "category": "гаджет",
                    "purchase_price": 50000,
                    "date_of_creation": "2023-09-30T17:28:14Z",
                    "last_modified_date": "2023-09-30T17:28:19Z"
                },
            ]

            product_for_create = []
            for product_item in product_list:
                product_for_create.append(Product(**product_item))

            #print(product_for_create)
            Product.objects.bulk_create(product_for_create)

            category_list = [
                {
                    "pk": 1,
                    "name": "Смартфон",
                    "description": "Телефон"
                },
                {
                    "pk": 2,
                    "name": "Электроинструмент",
                    "description": "Разный инструмент"
                },
                {
                    "pk": 3,
                    "name": "гаджет",
                    "description": "небольшое устройство"
                },
                {
                    "pk": 4,
                    "name": "Ручной инструмент",
                    "description": "Что держим в руках"
                }
            ]

            category_for_create = []
            for category_item in category_list:
                category_for_create.append(Category(**category_item))

            #print(category_for_create)
            Category.objects.bulk_create(category_for_create)
        except ProgrammingError:
            print("У нас ошибка")
        except IntegrityError as e:
            self.stdout.write('Invalid fixtures')
        else:
            self.stdout.write('Fixtures have been loaded')
