from django import forms
from .models import Product, Category, Subcategory, Brand
from cloudinary.models import CloudinaryField


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = CloudinaryField('image', blank=True, null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        subcategories = Subcategory.objects.all()
        brands = Brand.objects.all()
        c_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        s_friendly_names = [
                (s.id, s.get_friendly_name()) for s in subcategories]
        b_friendly_names = [(b.id, b.get_friendly_name()) for b in brands]

        self.fields['category'].choices = c_friendly_names
        self.fields['subcategory'].choices = s_friendly_names
        self.fields['brand'].choices = b_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
