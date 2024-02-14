from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('clients/', views.clients, name='clients'),
    path('product/', views.product, name='product'),
    path('order/', views.order, name='order'),
    path('sorting_orders_date/<int:client_id>/<int:duration>', views.sorting_orders_date, name='sorting_orders_date'),
    path('sorting_orders_date_week/<int:client_id>', views.sorting_orders_date_week, name='sorting_orders_date_week'),
    path('sorting_orders_date_month/<int:client_id>', views.sorting_orders_date_month, name='sorting_orders_date_month'),
    path('sorting_orders_date_year/<int:client_id>', views.sorting_orders_date_year, name='sorting_orders_date_year'),
    path('products/add', views.product_form_add, name='product_form_add'),
]