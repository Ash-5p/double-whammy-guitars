from django.db import models
from cloudinary.models import CloudinaryField


class Subcategory(models.Model):
    """
    Stores a single subcategory
    """
    class Meta:
        verbose_name_plural = 'Subcategories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Category(models.Model):
    """
    Stores a single category
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    subcategory = models.ManyToManyField(
        'Subcategory', blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Stores a single product
    """
    category = models.ForeignKey(
            'Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey(
            'Subcategory', null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey(
            'Brand', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name
