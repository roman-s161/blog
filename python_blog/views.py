from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# from .blog_data import dataset
from .models import Post, Category


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
    posts = Post.objects.all()
    
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
    return HttpResponse("Каталог тегов")


def tag_detail(request, tag_slug):
    return HttpResponse(f"Страница тега {tag_slug}")
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.urls import reverse
# from django.utils.text import slugify

# from .blog_data import dataset, CATEGORIES





# def catalog_tags(request):
#     unique_tags = set()
#     for post in dataset:
#         unique_tags.update(post['hashtags'])

#     # global TAGS  # Объявляем TAGS глобальной
#     TAGS = [{'name': tag, 'slug': slugify(tag), 'posts': [p for p in dataset if tag in p['hashtags']]} for tag in unique_tags]

#     context = {
#         "title": "Теги",
#         "text": "Список всех тегов",
#         "tags": TAGS,
#         "active_page": "blog:tags",
#     }
#     return render(request, 'python_blog/catalog_tags.html', context)

# def tag_detail(request, tag_slug):
#     tag = next((tag for tag in TAGS if tag['slug'] == tag_slug), None)  # Используем next с значением по умолчанию

#     if tag:
#         name = tag['name']
#     else:
#         name = tag_slug

#     context = {
#         "title": f"Тег: {name}",
#         "text": f"Посты с тегом: {name}",
#     }
#     return render(request, 'python_blog/tag_detail.html', context)


# def main(request):
#     context: dict[str, str ] = {
#         "title": "Главная", 
#         "text": "Главная страница",
#         "user_status": "admin",
#         "active_page": "main",
#     }
#     return render(request, 'main.html', context)

# def about(request):
#     context: dict[str, str ] = {
#         "title": "О нас",
#         "text": "OOO Albatross",
#         "active_page": "about",
        
#     }
#     return render(request, 'about.html', context)

#     # catalog_categories_url = reverse('blog:categories')
#     # catalog_tags_url = reverse('blog:tags')

#     # return HttpResponse(f"""
#     #     <h1>Главная страница</h1>
#     #     <p><a href="{catalog_categories_url}">Каталог категорий</a></p>
#     #     <p><a href="{catalog_tags_url}">Каталог тегов</a></p>
#     # """)


# def catalog_posts(request):
#     posts = [post for post in dataset if post['is_published']]
#     context = {
#         "title": "Каталог постов",
#         "posts": posts,
#     }
#     # context: dict[str, str ] = {
#     #     "title": "Каталог постов",
#     #     "text": "Текст страницы каталога постов",
#     #     "active_page": "blog:posts",
#     #     "dataset": dataset,
#     # }
#     return render(request, 'python_blog/blog.html', context)

# # def post_detail(request, post_slug):
# #     return HttpResponse(f'Страница поста {post_slug}')
# def post_detail(request, post_slug):
#     # Находим нужный пост по slug
#     post = next((post for post in dataset if post['slug'] == post_slug), None)
    
#     context = {
#         'title': post['title'],
#         'post': post
#     }
#     return render(request, 'python_blog/post_detail.html', context)

# def catalog_categories(request):
#     links = []
#     for category in CATEGORIES:
#         url = reverse('blog:category_detail', args=[category['slug']])
#         links.append(f'<p><a href="{url}">{category["name"]}</a></p>')

#         context = {
#             "title": "Категории",
#             "text": "Текст страницы категорий",
#             "categories": CATEGORIES,
#             "active_page": "blog:categories",
#         }   
#         return render(request, 'python_blog/catalog_categories.html', context)
    

# def category_detail(request, category_slug):

#     category = [cat for cat in CATEGORIES if cat['slug'] == category_slug][0]
    
#     if category:
#         name = category['name']
#     else:
#         name = category_slug

#     context: dict[str, str] = {
#         "title": f"Категория: {name}",
#         "text": f"Текст категория: {name}"
#     }
#     return render(request, 'python_blog/category_detail.html', context)
        
   

# # def catalog_tags(request):
# #     return HttpResponse('Каталог тегов')

# # def tag_detail(request, tag_slug):
# #     return HttpResponse(f'Страница тега {tag_slug}')