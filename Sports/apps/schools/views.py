from rest_framework import viewsets
from rest_framework import mixins

from .serializers import SchoolSerializer3, SchoolSerializer1
from .models import Schools


class SchoolViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    # queryset = Schools.objects.filter(category_type=1)
    queryset = Schools.objects.all()
    serializer_class = SchoolSerializer3

