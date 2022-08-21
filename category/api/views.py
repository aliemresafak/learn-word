from rest_framework.viewsets import ModelViewSet

from category.api.serializers import CategorySerializer
from category.models import Category


class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
