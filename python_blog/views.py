from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# from .blog_data import dataset
from .models import Post, Category, Tag
from django.db.models import Count


def main(request):
    catalog_categories_url = reverse("blog:categories")
    catalog_tags_url = reverse("blog:tags")

    context = {
        "title": "Главная страница",
        "text": "Текст главной страницы",
        "user_status": "moderator",
    }
    return render(request, "main.html", context)


def about(request):
    context = {
        "title": "О компании",
        "text": "Мы - команда профессионалов в области веб-разработки",
    }
    return render(request, "about.html", context)

def catalog_posts(request):
    # Получаем все опубликованные посты из базы данных
    posts = Post.objects.select_related('category', 'author').prefetch_related('tags').all()
    
    context = {
        'title': 'Блог',
        'posts': posts
    }
    
    return render(request, 'python_blog/blog.html', context)
# def catalog_posts(request):
#     # Получаем все опубликованные посты
#     posts = [post for post in dataset if post['is_published']]
#     context = {
#         'title': 'Блог',
#         'posts': posts
#     }
#     return render(request, 'python_blog/blog.html', context)

def post_detail(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    context = {"title": post.title, "post": post}
    return render(request, "python_blog/post_detail.html", context)
# def post_detail(request, post_slug):
#     # Находим нужный пост по slug
#     post = next((post for post in dataset if post['slug'] == post_slug), None)
    
#     context = {
#         'title': post['title'],
#         'post': post
#     }
#     return render(request, 'post_detail.html', context)

def catalog_categories(request):
    CATEGORIES = Category.objects.all()

    context = {
        "title": "Категории",
        "text": "Текст страницы с категориями",
        "categories": CATEGORIES,
    }
    return render(request, "python_blog/catalog_categories.html", context)


def category_detail(request, category_slug):

    category = Category.objects.filter(slug=category_slug).first()
    posts = Post.objects.filter(category=category)

    return render(
        request, "python_blog/category_detail.html", {"category": category, "posts": posts}
    )


def catalog_tags(request):
    # Получаем все теги и аннотируем их количеством постов
    tags = Tag.objects.annotate(posts_count=Count('posts')).order_by('-posts_count')
    
    context = {
        'tags': tags,
        'title': 'Теги блога',
        'active_menu': 'tags'
    }
    return render(request, 'python_blog/catalog_tags.html', context)


def tag_detail(request, tag_slug):
    # Получаем все посты конкретного тега через многие-ко-многим
    tag = Tag.objects.get(slug=tag_slug)
    posts = tag.posts.all()

    context = {
        "tag": tag,
        "posts": posts,
        "title": f"Тег: {tag.name}",
        "active_menu": "tags",  # Добавляем флаг активного меню
    }


    return render(request, "python_blog/tag_detail.html", context)
