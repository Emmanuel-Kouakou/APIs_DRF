from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

from rest_framework.views import APIView

from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from rest_framework.response import Response

class CategoryAPIView(APIView):
    
    # un endpoint
    def get(self, *args, **kwargs):
        # On prend la collection
        categories = Category.objects.order_by('-date_created')

        # on serialise les données
        serializer = CategorySerializer(categories, many=True)

        # retourne les données sérialisées
        return Response(serializer.data)
    

    
class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.order_by('-date_created')
    serializer_class = CategorySerializer  


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.order_by('-date_created')
    serializer_class = ProductSerializer      
    

# Le paramètre  many  permet de préciser au Serializer qu’il va devoir générer une liste d’éléments à partir de l’itérable (notre queryset) qui lui est transmis.


class ProductAPIView(APIView):
    
    def get(self, *args, **kwargs):
        products = Product.objects.order_by('-date_created')
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)