from django import forms
from  catalog.models import Product, Possibilities


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('name', )
        # exclude = ('is_active',)'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        exception = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', ]
        if cleaned_data in exception:
            raise forms.ValidationError('Запрещенный продукт')

        return cleaned_data

class PossibilitiesForm(forms.ModelForm):
    class Meta:
        model = Possibilities
        fields = '__all__'
