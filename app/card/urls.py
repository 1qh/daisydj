from django.urls import path
from rest_framework import routers

from .views import (
    ArtifactAnnotationViewSet,
    ArtifactStarViewSet,
    ArtifactViewSet,
    ClientViewSet,
    VersionHistoryViewSet,
    VersionViewSet,
    artifact_list,
)

router = routers.DefaultRouter()
router.register(r'artifacts', ArtifactViewSet)
router.register(r'annotations', ArtifactAnnotationViewSet)
router.register(r'star', ArtifactStarViewSet)
router.register(r'client', ClientViewSet)
router.register(r'version', VersionViewSet)
router.register(r'version_history', VersionHistoryViewSet)


urlpatterns = router.urls
