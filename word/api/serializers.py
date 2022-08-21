from rest_framework.serializers import ModelSerializer

from category.api.serializers import CategorySerializer
from word.models import Word


class WordSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Word
        fields = ("name", "meaning", "category")
