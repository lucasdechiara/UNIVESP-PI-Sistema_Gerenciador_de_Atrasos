from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import RegAtrasosViewSet, relatorio_atrasos_por_ra

router = DefaultRouter()
router.register(r'registros', RegAtrasosViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/relatorio_atrasos/<str:ra>/', relatorio_atrasos_por_ra, name='relatorio_atrasos_ra'),
]