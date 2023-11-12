from django import forms

from catalog.models import Product, Version


class StyleFormMixin:

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs.update({
    #             'class': 'form-control',
    #             'autocomplete': 'off'
    #         })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user',)
        # fields = ('product_name', 'product_description', 'product_preview', 'product_category', 'product_price',)

    def clean_product_name(self):
        exception = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')
        clean_data_name = self.cleaned_data['product_name']

        if clean_data_name.lower() in exception:
            raise forms.ValidationError('Данный продукт под санкциями ;)')
        return clean_data_name

    def clean_product_description(self):
        exception = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')
        clean_data_description = self.cleaned_data['product_description']

        if clean_data_description.lower() in exception:
            raise forms.ValidationError('Описание продукта нужно поменять ;)')
        return clean_data_description


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
