from django.urls import include, path
from rest_framework.routers import SimpleRouter

from users.api.views import UserViewSet

router = SimpleRouter()
router.register("", UserViewSet)


urlpatterns = [
    path("users/", include(router.urls)),
    path("token/", include("users.token.urls")),
]
