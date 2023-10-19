from django import forms
from  catalog.models import Product, Possibilities


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('name', )
        # exclude = ('is_active',)'


class PossibilitiesForm(forms.ModelForm):
    class Meta:
        model = Possibilities
        fields = '__all__'
