from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('clients/', views.clients, name='clients'),
    path('product/', views.product, name='product'),
    path('order/', views.order, name='order'),
]