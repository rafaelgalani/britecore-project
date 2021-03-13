from rest_framework import viewsets
from ..models import Risk
from ..serializers import RiskSerializer

class RiskViewSet(viewsets.ModelViewSet):
    queryset = Risk.objects.all()
    serializer_class = RiskSerializer

