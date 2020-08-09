from django.shortcuts import render

from django.views.generic import TemplateView

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from django.http import JsonResponse

# Create your views here.
from .models import Category, Subcategory, Product
from .serializers import CategorySerializer, SubcategorySerializer, NewProductSerializer, ProductSerializer

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['post'])
    def addproduct(self, request, pk=None):
        print(request.data)

class NewProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = NewProductSerializer
