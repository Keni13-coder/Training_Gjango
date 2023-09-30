from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.core.handlers.wsgi import WSGIRequest
from django.views.generic import TemplateView
from .utils import Author, Post, Comments


class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello World from class')


def my_view(reuest: WSGIRequest):
    context = {'name': 'Max'}
    print(type(reuest))
    print(reuest.method)
    return render(request=reuest, template_name='less3app/index.html', context=context)


class Templif(TemplateView):
    template_name = 'less3app/templ_if.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['massage'] = 'Hello world'
        context['number'] = 5
        return context
    

def test_models(request: WSGIRequest, author_id: int):
    # post = Post.objects.filter(author=author_id).order_by('-id')[:5]
    author = get_object_or_404(Author, pk=author_id)
    post = Post.objects.filter(author=author).order_by('-id')[:5]

    return render(request=request, template_name='less3app/index.html')


def about(request: WSGIRequest):
    text = 'Бублик бабля'
    context = {'text': text}
    return render(request=request, template_name='less3app/about.html', context=context)



def author_posts(request: WSGIRequest, author_id: int):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    context = {'author': author, 'posts':posts}
    return render(request=request, template_name='less3app/author_posts.html', context=context)


def posts(request: WSGIRequest, post_id:int):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comments.objects.filter(post=post)
    post.count_views += 1
    post.save()
    return render(request=request, template_name='less3app/posts.html', context={'post': post, 'comments':comments})


# def create_comments(request: WSGIRequest):
#     for i in range(1,11):
#         for j in range(1,11):
#             author = get_object_or_404(Author, pk=i)
#             post = get_object_or_404(Post, pk=j)
#             comment = Comments(author=author, post=post, comment=f'Comment{i}-{i*j}')
#             comment.save()
