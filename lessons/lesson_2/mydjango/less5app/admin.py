from django.contrib import admin
from .models import Category, Product

# отображением занимается description


@admin.action(description='Сбросить количесво в ноль')
def reset_quantity(modeladmin, request, queryset):
    # queryset имеет представлении db, посмотреть какой класс
    queryset.update(quantity=0)


# отображение полей в админке
class ProductAdmin(admin.ModelAdmin):
    '''Список продуктов'''
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
    # fields = ['name', 'description', 'category', 'date_added', 'rating']
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
