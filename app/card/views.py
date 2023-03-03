from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.renderers import TemplateHTMLRenderer

from .filters import ArtifactFilter
from .models import (
    Artifact,
    ArtifactAnnotation,
    ArtifactStar,
    Client,
    Version,
    VersionHistory,
)
from .serializers import (
    ArtifactAnnotationSerializer,
    ArtifactSerializer,
    ArtifactStarSerializer,
    ClientSerializer,
    VersionHistorySerializer,
    VersionSerializer,
)


@login_required
def artifact_list(request):
    clients = Client.objects.all()
    versions = Version.objects.all()
    selected_clients = request.GET.getlist('clients')
    selected_versions = request.GET.getlist('versions')

    # Add a `selected` flag to each client and version
    for client in clients:
        client.selected = str(client.pk) in selected_clients
    for version in versions:
        version.selected = str(version.pk) in selected_versions

    # Filter artifacts based on selected clients and versions
    artifacts = Artifact.objects.all()
    if selected_clients:
        artifacts = artifacts.filter(device_version__client__in=selected_clients)
    if selected_versions:
        artifacts = artifacts.filter(device_version__version__in=selected_versions)

    context = {
        'artifacts': artifacts,
        'clients': clients,
        'versions': versions,
    }
    return render(request, 'card/index.html', context)


class CustomRender(TemplateHTMLRenderer):
    def get_template_context(self, data, renderer_context):
        context = {'data': data}
        response = renderer_context['response']
        if response.exception:
            data['status_code'] = response.status_code
        return context


class ArtifactViewSet(viewsets.ModelViewSet):
    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = ArtifactFilter
    search_fields = ['video_path']
    ordering_fields = ['video_path']


class ArtifactAnnotationViewSet(viewsets.ModelViewSet):
    queryset = ArtifactAnnotation.objects.all()
    serializer_class = ArtifactAnnotationSerializer
    filter_backends = [DjangoFilterBackend]


class ArtifactStarViewSet(viewsets.ModelViewSet):
    queryset = ArtifactStar.objects.all()
    serializer_class = ArtifactStarSerializer
    filter_backends = [DjangoFilterBackend]


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]


class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer
    filter_backends = [DjangoFilterBackend]


class VersionHistoryViewSet(viewsets.ModelViewSet):
    queryset = VersionHistory.objects.all()
    serializer_class = VersionHistorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client']
