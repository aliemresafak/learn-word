from rest_framework.routers import DefaultRouter

from word.api.views import WordViewset

word_router = DefaultRouter()
word_router.register("words", WordViewset, basename="word")
