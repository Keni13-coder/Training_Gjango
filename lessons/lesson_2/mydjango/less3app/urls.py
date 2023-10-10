from django.urls import path
from .views import HelloView, my_view, Templif, test_models, about, author_posts, posts

urlpatterns = [
    # path('hello/', HelloView.as_view(), name='hello'),
    # path('hello/<int:year>/<int:mount>', HelloView.as_view(), name='hello_date'),
    # path('if/', Templif.as_view(), name='templ_if'),
    # path('test/<int:author_id>', test_models, name='test'),
    path('about/', about, name='about'),
    path('author_posts/<int:author_id>', author_posts, name='author_posts'),
    path('post/<int:post_id>', posts, name='post'),
    # path('create_comments', create_comments, name='create_comments')
]