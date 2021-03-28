from django.db import models


# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Occasion(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    occasion = models.ManyToManyField('Occasion')
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    product_image = models.ImageField(null=False, blank=True)

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.category, self.occasion)


class Color(models.Model):
    name = models.CharField(max_length=254)
    product_id = models.ManyToManyField('Product')

    def __str__(self):
        return '{}'.format(self.name)


class Flower(models.Model):
    name = models.CharField(max_length=254)
    product_id = models.ManyToManyField('Product')

    def __str__(self):
        return '{}'.format(self.name)
