from rest_framework import serializers

from .models import (
    Artifact,
    ArtifactAnnotation,
    ArtifactStar,
    Client,
    Version,
    VersionHistory,
)


class ArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artifact
        fields = '__all__'


class ArtifactAnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtifactAnnotation
        fields = '__all__'


class ArtifactStarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtifactStar
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'


class VersionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionHistory
        fields = '__all__'
