from django.contrib import admin
from storeapp.models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name_client', 'email_client', 'phone_client', 'adress_client', 'date_client']
    search_fields = ['name_client', 'email_client', 'phone_client']
    ordering = ['-date_client']
    list_filter = ['name_client']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name_product', 'text_product', 'price_product', 'quantity_product', 'date_product', 'image_product']
    search_fields = ['name_product', 'price_product', 'quantity_product']
    ordering = ['name_product']
    list_filter = ['name_product']

    fieldsets = [
        (
            'Общая информация',
            {
                'classes': ['wide'],
                'fields': ['name_product', 'text_product', 'image_product'],
            },
        ),
        (
            'Бух учет',
            {
                'classes': ['collapse'],
                'fields': ['price_product', 'quantity_product'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client_order', 'price_order', 'date_order']
    search_fields = ['client_order', 'price_order', 'date_order']
    ordering = ['-date_order']
    list_filter = ['date_order']



admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
# Register your models here.
