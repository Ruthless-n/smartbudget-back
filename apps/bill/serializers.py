from rest_framework import serializers
from apps.core.models import Bill
from apps.user.serializers import UserSerializer
from apps.category.serializer import CategorySerializer
from apps.status.serializers import StatusSerializer

class BillSerializer(serializers.ModelSerializer):

    responsible = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    
    class Meta:
        model = Bill
        fields = '__all__'