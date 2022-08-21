from rest_framework.routers import DefaultRouter

from authentication.api.views import UserViewset

users_router = DefaultRouter()
users_router.register("users", UserViewset, basename="users")
