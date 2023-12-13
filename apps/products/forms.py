from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].empty_label = "Category not selected"

    class Meta:
        model = Product
        fields = ('name', 'model', 'amount', 'currency', 'count', 'description', 'size',
                  'color', 'rate', 'brand', 'photo', 'video', 'categories')
