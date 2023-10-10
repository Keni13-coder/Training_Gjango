'django-admin startproject name_project - создание начального каркаса django'
'python manage.py startapp myapp - создание каталога с приложением'
'после создание каталога не забываем добовлять его название в натройки'
'python manage.py makemigrations name_app - по факту определяет наши модели в базе дынных, если не указывать name_app то модели определяться во всех приложениях проекта'
'python manage.py migrate - иницилизация наших файлов из migrations в базу данных'
'python manage.py createsuperuser - создание суперпользователя'
'''
INSTALLED_APPS = [
    myapp,
]
'''
'asgi - асинхронный подход'
'wsgi - синхронный подход'

'''
пишится в файл настроек
# позволяет добавить хосты для подключения
# возможность подключаться с 1 локальной сетью
ALLOWED_HOSTS = [
    '192.168.0.235',
    '127.0.0.1'
]
'''
'''
когда создаем вьюшку добовляем в urls джанги использовав include, так же в самом каталоге
с приложением создаем urls и определяем маршрут. По факту в вашем urls будет тож самое что и в проекте
'''


'''
LOGING = {} - настройка логирования

'''

'''
создание команд чтоб в консоли узать после manage.py
management - пакет
    __init__.py
    commands - пакет
    __init__.py
    my_command
в самом фале создаем классы на основе
from django.core.management.base import BaseCommand
там и описываем функционал команд
в консоле делам python manage.py my_command
'''


'''
DATABASES
обращение происходет через модель
для чтения
Model.objects.all
Model.objects.get
Model.objects.filter
при выборе лучше использовать filter
в filter можно использовать дополнительные праметры поиска
напрмер:
    Model.objects.filter(name__gt).first()
    если не кказывать first то выбор будет всего
где name - параметр поиска а __gt являеться дополнительным параметром

для сохранения используем эксемпряр класса модели
user = User(**kwargs)
user.save()

обновление данный происходит через точку
user.name = new_name
user.save()
models = [model]
добовление сразу нескольких моделей в db
model.objects.bulk_create(models)

для суммирования
django.db.models import Sum
objects.aggregate(Sum('column_name'))

для удаления
user.delete()

для связи используем оъбект query
pk = первичный ключ являеться индификатором записи
например:
    author = Author.objects.filter(pk=pk)
    posts = Post.objects.filter(author=author)
    где author в поле Post являеться внешним ключем
    
Так же можно использовать непросредственно только Post
например:
    posts = Post.objects.filter(author__pk=pk)
'''

'''
JsonResponse() - если нужно вернуть только json object

TEMPLATES - в настройках указываем такой синтаксис для указание главной папки
        'DIRS': [
            BASE_DIR/ 'templates'
            ],
            
папка templates будет находиться в корневой папке всех приложейни на одно уровне вместе с manage
в папке будет 1 шаблом base от которого все наследуются
наследование {% extends 'base.html' %}
'''

'''
from django.shortcuts import get_object_or_404
позволяет работать с базой данных, если не нашло возвращает 404
например:
def test(request, author_id: int)
    author = get_object_or_404(Author, pk=author_id)
    post = Post.objects.filter(author=author)
нужен для того чтобы сразу обработать существование записи
если записи нет то ошибка 404
опредеалем в urls и если было найдено то будет страничка иначе ошибка 404
'''

'''
Валидация своя в классе от Form
clean_<name> - где name являеться наименованием поля в классе
вслучие True возвращает поле return <name>
'''
'''
Подготовка к сохранению файлов
setting
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.changed_data['image']
            fs = FileSystemStorage()
            fs.save(name=image.name, content=image )
'''

'''
LANGUAGE_CODE = 'en-us'
на 
LANGUAGE_CODE = 'ru-ru'
'''
'''

'''

'''
models.py
    description = models.TextField(default='', blank=True)
blank=True при создании модели говорит о том что это поле не обязательно для заполнения
'''


'''
                ADMIN

супер пользователь
python manage.py createsuperuser


from .models import Category, Product

# отображением занимается description


@admin.action(description='Сбросить количесво в ноль')
def reset_quantity(modeladmin, request, queryset):
    # queryset имеет представлении db, посмотреть какой класс
    queryset.update(quantity=0)


# отображение полей в админке
class ProductAdmin(admin.ModelAdmin):
    # общее отображение
    list_display = ['name', 'category', 'quantity']
    # сортировка
    ordering = ['category', '-quantity']
    # добовляет с права филтр
    list_filter = ['date_added', 'price']
    # добоавляет поля для поиска
    search_fields = ['description']
    # подсказка под полем ввода
    search_help_text = 'Поиск по полю Описание продукта (description)'
    # подключает функции
    actions = [reset_quantity]

    # отображение полей непросредственно в продукте
    fields = ['name', 'description', 'category', 'date_added', 'rating']
    # поля только для чтение
    readonly_fields = ['date_added', 'rating']
    # поле взаимоискючающиеся fields and fieldsets
    fieldsets = [
        (None, {'classes': ['wide'], 'fields':['name']}),
        ('Подробности', {'classes': ['collapse'], 'description': 'Категория товара и его подробности', 'fields': [
         'category', 'description']}),
        ('Бухгфлнерия', {'fields':['price', 'quantity']}),
        ('Рейтинг и прочее', {'description': 'Рейтинг сформирован автоматически на основе оценок покупателей', 'fields': ['rating', 'date_added']})
    ]
    # classes отвечают за вид отображения
    # collapse - схлопнувшиеся поля
    # wide широкое поле
    # field - поля отображение
    # description - описание отсека, будет под именем

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)


            ИЗМЕНЕНИЕ ИМЕНИ ОТОБРАЖЕНИЯ В АДМИНКЕ

    ФАЙЛ apps.py
    
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class Less5AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'less5app'
    verbose_name = _("Товары и категории")
    
    
меняем именя для отображение в приложении панели в адменке
прописываем в моделе
    class Meta:
        verbose_name = 'Авторы'
        verbose_name_plural = 'Авторы'
'''


'''
                        django-debug-toolbar

pip install django-debug-toolbar

INTERNAL_IPS = [
    '127.0.0.1'
]

INSTALLED_APPS=[
+    debug_toolbar
]

MIDDLEWARE = [
+    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

urlpatterns = [
+    path('__debug__/', include('debug_toolbar.urls')),
]
'''

'''
                    Подготовка для развертывания
на сайте databases создаем пароль для подключение к db
нажатие на имя для вызва консоли
пишим:
    # username - ваш ник при регистрации
    ALTER DATABASE username$default CHARACTER SET utf8 COLLATE utf8_general_ci;
кликаем по имени
после перенос данных для конекта, после создание пароля будет страница с данными
в DATABASES = {
    default:{
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'username$default'
        'USER': 'username'
        'PASSWORD': os.getenv('MYSQL_PASSWORD')
        'HOST': 'username.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET NAMES 'utf8mb4';SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4'
        }
    }
}
import os
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
ALLOWED_HOSTS = [
    '127.0.0.1',
    # name - имя при регистрации на сайте
    'name.pythonanywhere.com'
]
STATIC_ROOT = BASE_DIR / STATIC_URL

создаем
pip freeze > requirements.txt
добовляем
+
    mysqlclient
    python-dotenv
коментируем
urlpatterns = [
#
    path('__debug__/', include('debug_toolbar.urls')),
]


1. dashboard
2. new console
3. bash
    git clone my_url
    # создание виртуального окружение
    # смотрим какая дупустимая версия для сайта pythonanywhere на момент видео max 3.10
    mkvirtualenv --python=/usr/bin/python3.10 virtualenv
    # переходим в папку с проектом
    # если создали папку в гите deployment_of_django, в ней уже то что переносили
    cd deployment_of_django
    pip install -r requirements.txt

1. Web
2. Add a new web app
    Manual configuration
    python 3.10
    
3. Web-Virtualenv
    откроем еще 1 страницу files
    смотрим в папках на сайте ищем виртуальное окружение
    копируем путь. добовляем в пункт

4. Code
    source code - дериктория приложений (там где все приложения)

5. WSGI configuration file - кликаем
    в фале смотрим на 74 строка
    стираем и вставляем
    # +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys
from dotenv import load_dotenv
# myproject название папки с приложениями
project_folder = os.path.expanduser('~/myproject') # adjust as
appropriate
load_dotenv(os.path.join(project_folder, '.env'))
## assuming your django settings file is at
'/home/username/mysite/mysite/settings.py'
## and your manage.py is is at '/home/username/mysite/manage.py'
path = '/home/username/myproject'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

6. Web-Virtualenv
    # ссылка на вирт окр
    start a console
    python
    import secrets
    secrets.token_hex() - copy token
    exit()
    echo 'export SECRET_KEY=token' >> .env
    echo 'export MYSQL_PASSWORD=herosiegemama2000fg' >> .env
    echo 'set -a; source ~/myproject/.env; set +a' >> ~/.virtualenvs/virtualenv/bin/postactivate
    exit


7. Files
    
    myproject
        # создаем log файл
        log -> New directory



8. Web-URL
    /static/      dir=home/username/myproject/static
    
9. Web-Virtualenv
    start a console
        python manage.py migrate
        python manage.py collectstatic
        python manage.py createsuperuser


10.  Configuration for myurl
    сам сайт
'''