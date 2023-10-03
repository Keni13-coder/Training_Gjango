'django-admin startproject name_project - создание начального каркаса django'
'python manage.py startapp myapp - создание каталога с приложением'
'после создание каталога не забываем добовлять его название в натройки'
'python manage.py makemigrations name_app - по факту определяет наши модели в базе дынных, если не указывать name_app то модели определяться во всех приложениях проекта'
'python manage.py migrate - иницилизация наших файлов из migrations в базу данных'
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