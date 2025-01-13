from django.contrib import admin
from .models import Category, Post, Tag
# Регистрация 2 способами
"""
1. Регистрация с использованием функции register
2. Регистрация с использованием класса
"""

# 1. Регистрация с использованием функци и декоратора
admin.site.register(Category)

# 2. Регистрация с использованием класса
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    # Поля, которые будут отображаться в списке постов
    list_display = ["title", "created_at", "updated_at", "category"]
    # Сделаем так, чтобы slug отображался но нельзя было редактировать
    readonly_fields = ["slug"]

class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ["name", "slug"]
    readonly_fields = ["slug"]


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)