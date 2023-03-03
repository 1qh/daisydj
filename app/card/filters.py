import django_filters

from .models import Artifact


class ArtifactFilter(django_filters.FilterSet):
    client = django_filters.CharFilter(field_name='device_version__client__client')
    version = django_filters.CharFilter(field_name='device_version__version__version')

    class Meta:
        model = Artifact
        fields = ['client', 'version']
