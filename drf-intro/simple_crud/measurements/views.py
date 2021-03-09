from rest_framework.viewsets import ModelViewSet

from measurements.models import Project, Measurement
from measurements.serializers import ProjectSerializer, MeasurementSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all().prefetch_related('measurements')
    serializer_class = ProjectSerializer


class MeasurementViewSet(ModelViewSet):
    queryset = Measurement.objects.all().select_related('project')
    serializer_class = MeasurementSerializer