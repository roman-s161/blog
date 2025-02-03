"""
Контекстный процессор передающий меню в каждый из шаблонов Джанго!
Не забудьте подключить это в в settings.py -> TEMPLATES -> context_processors
'python_blog.context_processors.menu_items', 
"""


def menu_items(request):
    menu = [
    {"title": "Главная", "url_name": "main"},
    {"title": "О нас", "url_name": "about"},
    {"title": "Все посты", "url_name": "blog:posts"},
    {"title": "Создать пост", "url_name": "blog:post_create"},
    {"title": "Категории", "url_name": "blog:categories"},
    {"title": "Теги", "url_name": "blog:tags"},
]
    
    # Определяем активный пункт меню
    current_url_name = request.resolver_match.view_name
    
    for item in menu:
        item['is_active'] = current_url_name == item['url_name']
    
    return {'menu_items': menu}