from django import forms

from .models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'title',
            'description',
            'slug',
            'restaurant'
        )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'category',
            'title',
            'ingredients',
            'allergens',
            'description',
            'history',
            'weight',
            'image',
            'restaurant'
        )

    def clean_image(self):
        image = self.cleaned_data['image']
        if not image:
            raise forms.ValidationError('Please upload an image')
        return image
