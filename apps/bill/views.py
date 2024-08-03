from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.core.models import Bill
from .serializers import BillSerializer



@api_view(['POST', 'GET'])
def list_bills(request):

    if request.method == 'GET':

        return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        
    if request.method == 'POST':
        return Response({'message': 'ok'}, status=status.HTTP_200_OK)
    
    
    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['GET', 'PUT', 'DELETE'])
def detail_bills(request, id_bill):


    if request.method == 'GET':

        return Response({'message': 'ok'}, status=status.HTTP_200_OK)
        
    if request.method == 'PUT':
        return Response({'message': 'ok'}, status=status.HTTP_200_OK)
    

    if request.method == 'DELETE':
        return Response({'message': 'ok'}, status=status.HTTP_200_OK)
    

    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)