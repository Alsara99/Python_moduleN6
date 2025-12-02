from django import forms
from .models import Product
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', 'date_created', 'date_last_changed']


    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите имя'
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите описание'
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Вставьте картинку'
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите категорию'
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену'
        })

        self.fields['date_created'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите дату создания'
        })

        self.fields['date_last_changed'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите дату последнего обновления'
        })


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Price не может быть отрицательным')
        return price


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')
        bad_list = ['казино',
        'криптовалюта',
        'крипта',
        'биржа',
        'дешево',
        'бесплатно',
        'обман',
        'полиция',
        'радар'
        ]

        if name and description:
            for i in bad_list:
                if i in name:
                    self.add_error('name', f'Name не может содержать слово "{i}"')
                if i in description:
                    self.add_error('description', f'Description не может содержать слово "{i}"')

