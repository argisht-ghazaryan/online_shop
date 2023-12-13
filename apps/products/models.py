from django.contrib.auth.models import User
from django.db import models
from helpers.choices import MoneyTypeChoices, SizeTypeChoices, CategoriesTypeChoices
from helpers.uplod_files import upload_product_image


class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255, null=True, blank=True)
    count = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=15, decimal_places=1)
    currency = models.CharField(max_length=30, choices=MoneyTypeChoices.choices)
    description = models.TextField(null=True, blank=True)
    size = models.CharField(max_length=50, choices=SizeTypeChoices.choices, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    # brand = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to=upload_product_image)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    categories = models.ForeignKey('Categories', on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=255, choices=CategoriesTypeChoices.choices)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
