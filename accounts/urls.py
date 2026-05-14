from rest_framework.routers import DefaultRouter
from .views import EmailAccountViewSet

router = DefaultRouter()

router.register('', EmailAccountViewSet)

urlpatterns = router.urls