from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.core.models import Bill
from .serializers import BillSerializer
from datetime import datetime
from django.db.models import Sum

@api_view(['POST', 'GET'])
def list_bills(request):
    if request.method == 'GET':
        responsible = request.query_params.get('responsible', None)
        status_filter = request.query_params.get('status', None)
        
        bills = Bill.objects.all()

        if responsible is not None:
            bills = bills.filter(responsible=responsible)
        if status_filter is not None:
            bills = bills.filter(status=status_filter)
        
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

@api_view(['GET'])
def get_total(request):
    user = request.user
    responsible_id = request.query_params.get('responsible', None)
    category_id = request.query_params.get('category', None)
    start_date = request.query_params.get('start_date', None)
    end_date = request.query_params.get('end_date', None)
    
    if responsible_id:
        bills = Bill.objects.filter(responsible=responsible_id).aggregate(total_spent=Sum('amount'))
    elif category_id:
        bills = Bill.objects.filter(category=category_id).aggregate(total_spent=Sum('amount'))
    elif start_date and end_date:
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            bills = Bill.objects.filter(due_date__range=[start_date, end_date]).aggregate(total_spent=Sum('amount'))
        except ValueError:
            return Response({'message': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        bills = Bill.objects.filter(responsible=user.id).aggregate(total_spent=Sum('amount'))

    return Response(bills, status=status.HTTP_200_OK)