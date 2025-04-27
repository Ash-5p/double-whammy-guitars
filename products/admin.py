from django.contrib import admin
from .models import Product, Category, Subcategory, Brand

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subcategory', 'brand', 'price')
    ordering = ('category', 'subcategory', 'name')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "subcategory":
            if request._obj_ is not None:
                kwargs["queryset"] = request._obj_.category.subcategory.all()
            else:
                kwargs["queryset"] = Subcategory.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        request._obj_ = obj
        return super().get_form(request, obj, **kwargs)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('friendly_name', )
    search_fields = ['name', 'friendly_name']
    filter_horizontal = ('subcategory',)


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):

    list_display = ('friendly_name', )
    search_fields = ['name', 'friendly_name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):

    list_display = ('friendly_name', )
    search_fields = ['name', 'friendly_name']
