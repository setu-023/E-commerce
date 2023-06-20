from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from store.models import *
from store.serializers import *

# class ProductList(generics.ListCreateAPIView):
class ProductList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Product.objects.all()
        serializer = ProductSerializer(snippets, many=True)
        return Response(serializer.data)
