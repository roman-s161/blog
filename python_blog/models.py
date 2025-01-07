# from django.db import models

# class Post(models.Model):
#     title = models.CharField(max_length=100, unique=True)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     category = models.CharField(null=True, blank=True, max_length=100)

from django.db import models
from unidecode import unidecode


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # категория - внешний ключ
    category = models.ForeignKey(
        "Category", # Ссылка на модель Category
        on_delete=models.SET_NULL, # При удалении категории, установить значение NULL
        blank=True, # Не требуем в формах заполнения
        null=True, # Разрешаем значение NULL в базе данных
        related_name="posts", # Имя обратной связи
        default=None # По умолчанию значение NULL
    )


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True, null=True, default="Без описания")