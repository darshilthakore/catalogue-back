from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"

class Subcategory(models.Model):
    name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategory")

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="productcat")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name="productsubcat")

    def __str__(self):
        return f"{self.name} | {self.subcategory} | {self.category}"

