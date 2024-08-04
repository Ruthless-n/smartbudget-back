from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.core.models import Role
from .serializers import RoleSerializer


@api_view(['POST', 'GET'])
def list_category(request):

    if request.method == 'GET':
        categories = Role.objects.all()
        serializer = RoleSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response({'message': 'Method not allowed'}, status=status.HTTP_200_OK)

