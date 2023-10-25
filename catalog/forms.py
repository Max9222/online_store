from django import forms
from catalog.models import Product, Possibilities, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        # fields = ('name', )
        exclude = ('anonymous_users',)


    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        exception = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', ]
        if cleaned_data in exception:
            raise forms.ValidationError('Запрещенный продукт')

        return cleaned_data

class PossibilitiesForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Possibilities
        fields = '__all__'


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
