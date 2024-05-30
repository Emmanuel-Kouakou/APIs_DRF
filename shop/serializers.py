
from .models import Category, Product

from rest_framework.serializers import ModelSerializer

class CategorySerializer(ModelSerializer):

    class Meta:

        model = Category
        fields = ['id', 'name', 'date_created', 'date_updated']



class ProductSerializer(ModelSerializer):

    class Meta:

        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category']        