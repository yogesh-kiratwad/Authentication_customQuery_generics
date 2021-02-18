from rest_framework.routers import DefaultRouter
from rest_framework import authentication
from .views import PostView

router = DefaultRouter()
router.register('api',PostView, basename='post')
urlpatterns = router.urls
