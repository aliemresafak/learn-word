from rest_framework.viewsets import ModelViewSet

from word.api.serializers import WordSerializer
from word.models import Word


class WordViewset(ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
