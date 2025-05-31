from django import forms
from .models import Product, Category, Subcategory, Brand


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'image': 'Image',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        subcategories = Subcategory.objects.all()
        brands = Brand.objects.all()

        self.fields['category'].choices = [
            (c.id, c.get_friendly_name()) for c in categories]
        self.fields['subcategory'].choices = [
            (s.id, s.get_friendly_name()) for s in subcategories]
        self.fields['brand'].choices = [
            (b.id, b.get_friendly_name()) for b in brands]

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
