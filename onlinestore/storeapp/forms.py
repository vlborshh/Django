from django import forms
import datetime

class ProductFormWidget(forms.Form):
    name_product = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                'placeholder': 'Наименование товара'}))
    text_product = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                                'placeholder': 'Описание товара'}))
    price_product = forms.FloatField(min_value=10, max_value=1_000_000,
                                     widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Стоимость товара'}))
    quantity_product = forms.IntegerField(min_value=0, max_value=10,
                                          widget=forms.NumberInput(attrs={'class': 'form-control',
                                                                'placeholder': 'В наличии'}))
    date_product = forms.DateField(initial=datetime.date.today,
                                   widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date',
                                                               'placeholder': 'Дата добавления товара'}))
    image_product = forms.ImageField(widget=forms.FileInput())

