from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.core.models import Status
from apps.status.serializers import StatusSerializer

@api_view(['GET'])
def status_list(request):
    statuses = Status.objects.all()
    serializer = StatusSerializer(statuses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

