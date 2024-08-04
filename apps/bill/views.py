from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.core.models import Bill
from .serializers import BillSerializer


    

@api_view(['POST', 'GET'])
def list_bills(request):

    if request.method == 'GET':
        bills = Bill.objects.all()
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    if request.method == 'POST':
        data = request.data
        if isinstance(data, list):
            serializer = BillSerializer(data=data, many=True)
        else:
            serializer = BillSerializer(data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def detail_bills(request, id_bill):

    if request.method == 'GET':
        try:
            bill = Bill.objects.get(id_bill=id_bill)
        except Bill.DoesNotExist:
            return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer =  BillSerializer(bill)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    if request.method == 'PUT':
        try:
            bill = Bill.objects.get(id_bill=id_bill)
        except Bill.DoesNotExist:
            return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BillSerializer(bill, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    

    if request.method == 'DELETE':
        try:
            bill = Bill.objects.get(id_bill=id_bill)
        except Bill.DoesNotExist:
            return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        
        bill.delete()
        return Response({'message': 'ok'}, status=status.HTTP_200_OK)
    

    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def list_bills_by_user(request, responsible):
    if request.method == 'GET':
        bills = Bill.objects.filter(responsible=responsible)
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)