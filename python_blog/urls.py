

from django.contrib import admin
from django.urls import path
from python_blog.views import catalog_posts, post_detail, catalog_categories, category_detail, catalog_tags, tag_detail

# Общий префикс posts/
urlpatterns = [
    # Каталог  постов posts/
    path('', catalog_posts),
    
    # Категории
    # Категории posts/categories/
    # Категории posts/categories/python/
    path('categories/', catalog_categories),
    path('categories/<slug:category_slug>/', category_detail),
    
    # Теги posts/tags/
    # Теги posts/tags/python/
    path('tags/', catalog_tags),
    path('tags/<slug:tag_slug>/', tag_detail),
    
    # Посты posts/tags/
    path('<slug:post_slug>/', post_detail),
]