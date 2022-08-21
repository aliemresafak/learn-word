from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from authentication.urls import users_router
from category.urls import category_router
from word.urls import word_router

router = DefaultRouter()

router.registry.extend(users_router.registry)
router.registry.extend(category_router.registry)
router.registry.extend(word_router.registry)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
