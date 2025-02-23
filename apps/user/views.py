from rest_framework.decorators import api_view, permission_classes
from django.urls import path, include
from rest_framework.response import Response
from rest_framework import status
from .models import UserCustomuser
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['GET','POST'])
def create_user(request):
    if request.method == 'GET':
        users = UserCustomuser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        request_email = request.data.get('email')
        if UserCustomuser.objects.filter(email=request_email).exists():
            return Response({'error': 'Error in credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = UserSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def detail_user(request, id_user):
    try:
        user = UserCustomuser.objects.get(id=id_user)
    except UserCustomuser.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


    if(request.method == 'GET'):
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
                        
    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def user_data(request):
  
  if request.method == 'GET':
     
    user = request.user
      
    try:
      user = UserCustomuser.objects.get(id=user.id)
    except UserCustomuser.DoesNotExist:      
      return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
  return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def logout_view(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
    except Exception as e:
        print(Exception)
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)