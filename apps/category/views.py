from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.core.models import Category
from .serializer import CategorySerializer


@api_view(['POST', 'GET'])
def list_category(request):

    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response({'message': 'Method not allowed'}, status=status.HTTP_200_OK)



@api_view(['GET', 'PUT', 'DELETE'])
def detail_category(request, id_category):

    try:
        category = Category.objects.get(id_category=id_category)
    except Category.DoesNotExist:
        return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer =  CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    if request.method == 'DELETE':
        category.delete()
        return Response({'message': 'ok'}, status=status.HTTP_200_OK)
    

    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

