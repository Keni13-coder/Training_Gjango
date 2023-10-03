from django.forms import CharField, EmailField, IntegerField, Form, FloatField, BooleanField, DateField, ChoiceField, ImageField
# виджеты или widget нужны для дополнительных настрояк полей, пишуться в widget=NumberInput(attrs={class:'form-control'})
from django.forms import NumberInput, TextInput, EmailInput, CheckboxInput, DateInput, RadioSelect, Textarea
import datetime
from .models import Author

class UserForm(Form):
    name = CharField(max_length=50)
    email = EmailField()
    age = IntegerField(min_value=0, max_value=120)
    
    
class ManyFieldsForm(Form):
    name = CharField(max_length=50)
    email = EmailField()
    age = IntegerField(min_value=18)
    height = FloatField()
    # required говорит являеться ли поле обязателным по умолчанию True
    is_active =BooleanField(required=False)
    # Для отоброжение календаря используем виджет с датой и добовляем type:date
    birthdate = DateField(initial=datetime.date.today)
    # M для базы данных Male для пользователя
    gender = ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    
    
class ImageForm(Form):
    image = ImageField()
    
    




'''
Задание №1
Доработаем задачу про броски монеты, игральной кости и
случайного числа.
Создайте форму, которая предлагает выбрать: монета, кости,
числа.
Второе поле предлагает указать количество попыток от 1 до 64.
'''

class Game(Form):
    game = ChoiceField(choices=[('name_funktion','coin'), ('name_funktion','bones'), ('name_funktion','random_number')],
                       widget=RadioSelect()
                       )
    count = IntegerField(min_value=1, max_value=64)
    
    
    
    
'''
Задание №3
Продолжаем работу с авторами, статьями и комментариями.
Создайте форму для добавления нового автора в базу
данных.
Используйте ранее созданную модель Author
'''

class CreateAuthorForm(Form):
    name = CharField(min_length=3, max_length=50)
    second_name = CharField(min_length=3, max_length=50)
    email = EmailField()
    biography = CharField(min_length=4, max_length=120, widget=Textarea())
    date_birthday = DateField(initial=datetime.date.today ,widget=DateInput())
    
    
'''
Задание №4
Аналогично автору создайте форму добавления новой
статьи.
Автор статьи должен выбираться из списка (все доступные в
базе данных авторы).
'''


class CreatePostForm(Form):
    title = CharField(min_length=4, max_length=200)
    authors = ChoiceField(choices=[(field.id, field.name) for field in Author.objects.all()])
    category = CharField(min_length=5, max_length=100)
    active = BooleanField(required=False)