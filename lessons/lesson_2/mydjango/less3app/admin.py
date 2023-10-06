from django.contrib import admin
from .models import Author, Post



class AuthorAdmin(admin.ModelAdmin):
    '''Список авторов'''
    # общее отображение
    list_display = ['name', 'date_birthday']
    # сортировка
    ordering = ['name']
    # добовляет с права филтр
    list_filter = ['date_birthday']
    # добоавляет поля для поиска
    search_fields = ['biography']
    # подсказка под полем ввода
    search_help_text = 'Поиск по полю Описание продукта (biography)'
    # подключает функции

    # отображение полей непросредственно в продукте
    # fields = ['name', 'description', 'category', 'date_added', 'rating']
    # поля только для чтение
    readonly_fields = ['biography', 'date_birthday']
    # поле взаимоискючающиеся fields and fieldsets
    fieldsets = [
        (None, {'classes': ['wide'], 'fields':['name']}),
        ('Подробности', {'classes': ['collapse'], 'description': 'Автор и его подробности', 'fields': [
         'biography', 'email', 'second_name']}),
    ]

class PostAdmin(admin.ModelAdmin):
    '''Список постов'''
    # общее отображение
    list_display = ['title', 'category', 'count_views']
    # сортировка
    ordering = ['title', 'category', 'count_views', 'time']
    # добовляет с права филтр
    list_filter = ['category', 'count_views','time', 'active']
    # добоавляет поля для поиска 
    search_fields = ['content']
    # подсказка под полем ввода
    search_help_text = 'Поиск по полю Описание продукта (content)'
    # подключает функции

    # отображение полей непросредственно в продукте
    # fields = ['name', 'description', 'category', 'date_added', 'rating']
    # поля только для чтение
    readonly_fields = ['content', 'time', 'count_views']
    # поле взаимоискючающиеся fields and fieldsets
    fieldsets = [
        (None, {'classes': ['wide'], 'fields':['title']}),
        ('Подробности', {'classes': ['collapse'], 'description': 'Пост и его содержание', 'fields': [
         'content', 'time']}),
        ('Автор', {'fields': ['author']}),
        ('Популярность', {'description': 'Категория и просмотры', 'fields': ['category', 'count_views']})
    ]






admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)