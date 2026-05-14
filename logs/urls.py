from rest_framework.routers import DefaultRouter
from .views import EmailLogViewSet

router = DefaultRouter()

router.register('', EmailLogViewSet)

urlpatterns = router.urls