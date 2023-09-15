from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UploadedFileViewSet

router = routers.DefaultRouter()
router.register(r'uploaded-files', UploadedFileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
