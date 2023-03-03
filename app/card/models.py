from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Client(models.Model):
    client = models.CharField(
        max_length=255,
        primary_key=True,
    )


class Version(models.Model):
    version = models.CharField(
        max_length=255,
        primary_key=True,
    )


class VersionHistory(models.Model):
    version = models.ForeignKey(
        Version,
        on_delete=models.CASCADE,
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
    )


class Artifact(models.Model):
    video_path = models.CharField(
        max_length=255,
        primary_key=True,
    )
    device_version = models.ForeignKey(
        VersionHistory,
        max_length=255,
        on_delete=models.CASCADE,
    )


class ArtifactAnnotation(models.Model):
    artifact = models.ForeignKey(
        Artifact,
        on_delete=models.CASCADE,
    )
    is_abnormal = models.BooleanField()
    comment = models.CharField(max_length=255)
    annotator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )


class ArtifactStar(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    artifact = models.ForeignKey(
        Artifact,
        on_delete=models.CASCADE,
    )
