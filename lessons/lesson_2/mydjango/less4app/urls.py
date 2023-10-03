from django.urls import path
from .views import user_form, many_fields_form, upload_image, game, test

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('user/many/', many_fields_form, name='many_fields_form'),
    path('user/many/', many_fields_form, name='many_fields_form'),
    path('upload_image/', upload_image, name='upload_image'),
    path('game/', game, name='game'),
    path('test/', test, name='test'),
]