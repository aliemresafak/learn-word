from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from category.api.serializers import CategorySerializer
from category.models import Category
from word.models import Word


class WordSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        write_only=True, source="category", queryset=Category.objects.all()
    )

    class Meta:
        model = Word
        fields = ("name", "type", "meaning", "category", "category_id")

    def create(self, validated_data):
        return super().create(validated_data)
