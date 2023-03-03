from django.contrib import admin

from .models import (
    Artifact,
    ArtifactAnnotation,
    ArtifactStar,
    Client,
    Version,
    VersionHistory,
)

admin.site.register(
    [
        Artifact,
        ArtifactAnnotation,
        ArtifactStar,
        Client,
        Version,
        VersionHistory,
    ]
)
