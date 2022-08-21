from rest_framework.routers import DefaultRouter

from category.api.views import CategoryViewset

category_router = DefaultRouter()

category_router.register("categories", CategoryViewset, basename="category")
