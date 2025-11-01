# views da API

from rest_framework import viewsets, permissions
from .models import RegAtrasos
from .serializers import RegAtrasosSerializer

#função do relatório
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status


class RegAtrasosViewSet(viewsets.ModelViewSet):
    queryset = RegAtrasos.objects.all()
    serializer_class = RegAtrasosSerializer
    permission_classes = [permissions.IsAuthenticated]

    

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def relatorio_atrasos_por_ra(request, ra):
    registros = RegAtrasos.objects.filter(ra=ra).order_by('-data_atraso')
    if not registros.exists():
        return Response(
            {"mensagem": f"Nenhum registro encontrado para o RA {ra}."},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = RegAtrasosSerializer(registros, many=True)
    return Response(serializer.data)






