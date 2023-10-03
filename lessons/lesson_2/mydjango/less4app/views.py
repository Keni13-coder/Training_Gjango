from django.shortcuts import render
from .forms import UserForm, ManyFieldsForm, ImageForm, Game, CreatePostForm, Author
from django.core.handlers.wsgi import WSGIRequest
from django.core.files.storage import FileSystemStorage

def user_form(request: WSGIRequest):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.changed_data['name']
            email = form.changed_data['email']
            age = form.changed_data['age']
            
            
    else:
        form = UserForm
    return render(request=request, template_name='less4app/user_form.html' ,context={'form': form})

def many_fields_form(request: WSGIRequest):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
            print('Все ОК')
        
    else:
        form = ManyFieldsForm()
    return render(request=request, template_name='less4app/many_fields_form.html', context={'form': form})


def upload_image(request: WSGIRequest):
    if request.method =='POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(name=image.name, content=image )
            
    else:
        form = ImageForm()
    return render(request=request, template_name='less4app/upload_image.html', context={'form': form})



def game(request: WSGIRequest):
    if request.method == 'POST':
        form = Game(request.POST)
        if form.is_valid():
            print('OK')
            
    else:
        form = Game
        
    return render(request=request, template_name='less4app/game.html', context={'form': form})



def test(request: WSGIRequest):
    # author = Author(name='Гена', second_name='Петя', email='mail@mail.ru', biography='asdasoewhiuisudsuuyafstdfi')
    # author.save()
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            print('OK')
            
    else:
        form = CreatePostForm()
        
    return render(request=request, template_name='less4app/test.html', context={'form': form})

