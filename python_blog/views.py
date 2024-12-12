from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

CATEGORIES = [
    {'slug': 'python', 'name': 'Python'},
    {'slug': 'django', 'name': 'Django'},
    {'slug': 'postgresql', 'name': 'PostgreSQL'},
    {'slug': 'docker', 'name': 'Docker'},
    {'slug': 'linux', 'name': 'Linux'},
]

def main(request):
    context: dict[str, str ] = {
        "title": "Главная", 
        "text": "Главная страница",
        "user_status": "admin",
    }
    return render(request, 'python_blog/main.html', context)

    # catalog_categories_url = reverse('blog:categories')
    # catalog_tags_url = reverse('blog:tags')

    # return HttpResponse(f"""
    #     <h1>Главная страница</h1>
    #     <p><a href="{catalog_categories_url}">Каталог категорий</a></p>
    #     <p><a href="{catalog_tags_url}">Каталог тегов</a></p>
    # """)


def catalog_posts(request):
    return HttpResponse('Каталог постов')

def post_detail(request, post_slug):
    return HttpResponse(f'Страница поста {post_slug}')

def catalog_categories(request):
    links = []
    for category in CATEGORIES:
        url = reverse('blog:category_detail', args=[category['slug']])
        links.append(f'<p><a href="{url}">{category["name"]}</a></p>')

        context = {
            "title": "Категории",
            "text": "Текст страницы категорий",
            "categories": CATEGORIES,
        }   
        return render(request, 'python_blog/catalog_categories.html', context)
    

def category_detail(request, category_slug):

    category = [cat for cat in CATEGORIES if cat['slug'] == category_slug][0]
    
    if category:
        name = category['name']
    else:
        name = category_slug

    context: dict[str, str] = {
        "title": f"Категория: {name}",
        "text": f"Текст категория: {name}"
    }
    return render(request, 'python_blog/category_detail.html', context)
        
   

def catalog_tags(request):
    return HttpResponse('Каталог тегов')

def tag_detail(request, tag_slug):
    return HttpResponse(f'Страница тега {tag_slug}')