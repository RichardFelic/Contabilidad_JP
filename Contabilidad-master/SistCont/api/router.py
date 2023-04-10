from rest_framework.routers import DefaultRouter
from SistCont.api.views import AuxiliarApiViewSet

router_auxiliares= DefaultRouter()

router_auxiliares.register(prefix='SistCont', basename='SistCont', viewset=AuxiliarApiViewSet)