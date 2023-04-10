from rest_framework.viewsets import ModelViewSet
from SistCont.models import *
from SistCont.api.serializers import AuxiliarSerializer

class AuxiliarApiViewSet(ModelViewSet):
    serializer_class= AuxiliarSerializer
    queryset = Auxiliar.objects.all()