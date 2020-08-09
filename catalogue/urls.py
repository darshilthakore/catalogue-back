from django.urls import path
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import include

from . import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'subcategories', views.SubcategoryViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'add', views.NewProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]