from django.urls import path
from . import views

urlpatterns = [
    path('user_point/<method>', views.user_point, name='user_point'),
    path('prod_point/<method>', views.prod_point, name='prod_point'),
    path('order_point/<method>', views.order_point, name='order_point'),
    ]