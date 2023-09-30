from django.shortcuts import render
from django.http import HttpResponse
import random
import logging
from .models import HeadsTails
from .utils import CrudAuthor, CrudComments, CrudPost, Info

logger = logging.getLogger(__name__)

def heads_or_tails(request):
    responce = random.choice(['орёл', "решка"])
    logger.info(f'responce:{responce}')
    db = HeadsTails(title=responce)
    db.save()
    context = {'side': responce}
    return render(request=request, template_name='myapp/heads_or_tails.html', context=context)


def read_db(request):
    responce = random.randint(1,6)
    logger.info(f'responce:{responce}')
    db_read = HeadsTails.read_title(responce)

    return HttpResponse(db_read)


def creater_db(request):
    # author = CrudAuthor()
    post = CrudPost()
    comment = CrudComments()
    # author_data = {'name': 'Pupa', 'second_name':'Lupa', 'email':'ipads@mail.ru', 'biography':'ляля тополя', 'date_birthday':'2000-09-16'}
    # responce = author.create_post(author_data)
    post_data = {'title':'реки', 'content': 'что-то невероятно огромное', 'author_id': 1, 'category': 'чепуха'}
    responce = post.create_post(post_data)
    # comment_data = {'author_id': 1, 'post_id':1, 'comment':'что-то интересное'}
    # responce = comment.create_post(comment_data)
    return HttpResponse(responce)


def info(request):
    responce = Info
    # return HttpResponse(responce.get_all_comments_author(1))
    return HttpResponse(responce.get_all_posts_author(1))
    # return HttpResponse(responce.get_all_comments_post(1))

