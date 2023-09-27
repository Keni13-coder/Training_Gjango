'''
Задание №7
Создайте функции для работы с базой данных:
○ Поиск всех статей автора по его имени
○ Поиск всех комментариев автора по его имени
○ Поиск всех комментариев по названию статьи
Каждая из трёх функций должна иметь возможность
сортировки и ограничение выборки по количеству.
'''
from .models import Post, Author, Comments
from django.db.models.base import ModelBase


class Crud():
    model: ModelBase = None
    

    def get_all_post(self):
        responce = self.model.objects.all()
        return responce
        
        
    def get_post(self, pk: int):
        responce = self.model.objects.filter(pk=pk)
        return responce


    def create_post(self, data: dict):
        responce = self.model(**data)
        responce.save()
        return f'{self.model} create'
        
    def update_post(self, pk: int, data: dict):
        ...
        
    def delete_post(self, pk: int):
        responce= self.model.objects.filter(pk=pk)
        responce.delete()
        return f'{self.model} delete'
        

class CrudPost(Crud):
    model = Post


class CrudAuthor(Crud):
    model = Author


class CrudComments(Crud):
    model = Comments
    
    
'''
○ Поиск всех статей автора по его имени
○ Поиск всех комментариев автора по его имени
○ Поиск всех комментариев по названию статьи
'''
class Info:
    @staticmethod
    def get_all_posts_author(pk_author, limit:int=0, desc: str='' ):
        if limit:
            query = Post.objects.filter(author=pk_author).order_by(f'{desc}pk')[:limit]
        else:
            query = Post.objects.filter(author=pk_author).order_by(f'{desc}pk')[:]
        return query
    
    @staticmethod
    def get_all_comments_author(pk_author, limit:int=0, desc: str='' ):
        if limit:
            query = Comments.objects.filter(author_id=pk_author).order_by(f'{desc}pk')[:limit]
        else:
            query = Comments.objects.filter(author_id=pk_author).order_by(f'{desc}pk')[:]
        return query

    @staticmethod
    def get_all_comments_post(pk_post, limit:int=0, desc: str='' ):
        if limit:
            query = Comments.objects.filter(post=pk_post).order_by(f'{desc}pk')[:limit]
        else:
            query = Comments.objects.filter(post=pk_post).order_by(f'{desc}pk')[:]
        return query