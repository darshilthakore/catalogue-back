import json
from rest_framework import serializers
from .models import Category, Subcategory, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True)
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'category']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'subcategory_name', 'category_name']
    
    subcategory_name = serializers.SerializerMethodField('get_subcategory_name')
    category_name = serializers.SerializerMethodField('get_category_name')

    def get_category_name(self, obj):
        return obj.category.name

    def get_subcategory_name(self, obj):
        return obj.subcategory.name
    

class NewProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'subcategory']

    def create(self, data):
        m = data['category']
        print(data)

        cat = data['category']
        subcat = data['subcategory']

        prod = Product.objects.create(name=data['name'], category=cat, subcategory=subcat)
        prod.save()

        return prod
        # name = ser.data
        # cat = Category.objects.get(name=name['name'])
        # print(cat.id)
