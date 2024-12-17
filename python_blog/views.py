from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

MENU_ITEMS = [
    {"title": "Главная", "url_name": "main"},
    {"title": "Все посты", "url_name": "blog:posts"},
    {"title": "Категории", "url_name": "blog:categories"},
    {"title": "Теги", "url_name": "blog:tags"},
]

CATEGORIES = [
    {'slug': 'python', 'name': 'Python'},
    {'slug': 'django', 'name': 'Django'},
    {'slug': 'postgresql', 'name': 'PostgreSQL'},
    {'slug': 'docker', 'name': 'Docker'},
    {'slug': 'linux', 'name': 'Linux'},
]

dataset = [
    {
        "title": "Что нового в Python 3.10?",
        "slug": "chto-novogo-v-python-310",
        "post": " В версии Python 3.10 появилось множество улучшений и новых функций. Например, улучшенные операторы сравнения и структурированное сопоставление с образцом.",
        "hashtags": ["python", "новости", "выпуск"],
        "is_published": False,
        "views": 5832,
        "likes": 142,
        "comments": [
            {"username": "alex_dev", "text": "Отличное обновление!"},
            {"username": "pythonista", "text": "Эти нововведения сильно ускорят работу."}
        ]
    },
    {
        "title": "Django: основные команды",
        "slug": "django-osnovnye-komandy",
        "post": "Django предоставляет множество встроенных команд для работы с проектом. Например, команды для миграций, создания суперпользователей, и очистки кеша.",
        "hashtags": ["django", "команды", "быстрый старт"],
        "is_published": False,
        "views": 4901,
        "likes": 85,
        "comments": [
            {"username": "webdev_jane", "text": "Спасибо за статью! Эти команды точно пригодятся."},
            {"username": "john_doe", "text": "Организовал шпаргалку у себя на рабочем столе."}
        ]
    },
    {
        "title": "Как настроить Django Rest Framework",
        "slug": "kak-nastroit-django-rest-framework",
        "post": "Django Rest Framework делает создание REST API невероятно простым. В статье рассмотрены основные команды и настройки.",
        "hashtags": ["django", "rest", "api"],
        "is_published": True,
        "views": 6710,
        "likes": 201,
        "comments": [
            {"username": "api_guru", "text": "Этот фреймворк просто спасает!"},
            {"username": "dev_peter", "text": "Установил и настроил за пару минут. Спасибо!"}
        ]
    },
    {
        "title": "Советы по оптимизации Django приложений",
        "slug": "sovety-po-optimizacii-django-prilozhenij",
        "post": "Оптимизировать Django проекты можно несколькими способами, такими как использование кеша, подгонка запросов к базе данных и оптимизация шаблонов.",
        "hashtags": ["django", "оптимизация", "производительность"],
        "is_published": True,
        "views": 3102,
        "likes": 109,
        "comments": [
            {"username": "optimizator", "text": "Люблю делать проекты быстрее!"},
            {"username": "django_fan", "text": "Спасибо за ценные советы!"}
        ]
    },
    {
        "title": "Python: работа с асинхронными функциями",
        "slug": "python-rabota-s-asinhronnimi-funkciyami",
        "post": "В Python асинхронные функции позволяют легче работать с операциями ввода-вывода. Узнайте больше о 'async' и 'await'.",
        "hashtags": ["python", "async", "await"],
        "is_published": True,
        "views": 5122,
        "likes": 130,
        "comments": [
            {"username": "async_fan", "text": "Асинхронность - будущее!"},
            {"username": "sync_master", "text": "Полезное руководство, но всё ещё предпочитаю синхронный код."}
        ]
    },
    {
        "title": "Создаем блог с помощью Django",
        "slug": "sozdaem-blog-s-pomoshyu-django",
        "post": "С помощью Django можно легко создать блог. В этом руководстве мы рассмотрим основные шаги создания проекта.",
        "hashtags": ["django", "блог", "руководство"],
        "is_published": True,
        "views": 7123,
        "likes": 178,
        "comments": [
            {"username": "blogger_anna", "text": "Создала свой первый блог!"},
            {"username": "django_beginner", "text": "Очень подробное руководство, спасибо!"}
        ]
    },
    {
        "title": "Работа с сигналами в Django",
        "slug": "rabota-s-signalami-v-django",
        "post": "Сигналы в Django используются для выполнения кода при определённых событиях, таких как сохранение или удаление модели.",
        "hashtags": ["django", "сигналы", "код"],
        "is_published": True,
        "views": 3899,
        "likes": 95,
        "comments": [
            {"username": "signal_guru", "text": "Сигналы - удобный способ расширить функциональность!"},
            {"username": "code_monkey", "text": "Сложно для новичка, но полезно."}
        ]
    },
    {
        "title": "Роутинг в Django: маршруты и URL",
        "slug": "routing-v-django-marshruty-i-url",
        "post": "Django использует маршрутизацию для сопоставления URL с соответствующими видами. В этой статье рассказано, как правильно настроить маршруты.",
        "hashtags": ["django", "роутинг", "url"],
        "is_published": True,
        "views": 4920,
        "likes": 102,
        "comments": [
            {"username": "url_mapper", "text": "Наконец-то понял как работают URL в Django!"},
            {"username": "web_junior", "text": "Применяю эти советы в своем проекте!"}
        ]
    },
    {
        "title": "Разработка тестов в Django",
        "slug": "razrabotka-testov-v-django",
        "post": "Тесты позволяют убедиться в правильности работы приложения. Django предоставляет встроенные инструменты для написания тестов.",
        "hashtags": ["django", "тесты", "разработка"],
        "is_published": True,
        "views": 4410,
        "likes": 120,
        "comments": [
            {"username": "test_dev", "text": "Теперь мои приложения работают надёжнее!"}
        ]
    },
    {
        "title": "Настройка виртуальных окружений в Python",
        "slug": "nastroika-virtualnih-okruzhenij-v-python",
        "post": "Использование виртуальных окружений помогает изолировать зависимости различных проектов. В статье приведена пошаговая инструкция настройки окружения.",
        "hashtags": ["python", "virtualenv", "окружение"],
        "is_published": True,
        "views": 5299,
        "likes": 113,
        "comments": [
            {"username": "env_pro", "text": "Теперь все мои проекты отделены друг от друга!"},
            {"username": "python_newbie", "text": "Раньше не понимал, зачем нужны виртуальные окружения. Теперь ясно!"}
        ]
    }
]

def main(request):
    context: dict[str, str ] = {
        "title": "Главная", 
        "text": "Главная страница",
        "user_status": "admin",
        "menu_items": MENU_ITEMS,
    }
    return render(request, 'main.html', context)

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