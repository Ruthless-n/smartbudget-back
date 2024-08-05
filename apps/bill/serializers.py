from rest_framework import serializers
from apps.core.models import Bill, Category, Status, UserCustomuser
from apps.user.serializers import UserSerializer
from apps.category.serializer import CategorySerializer
from apps.status.serializers import StatusSerializer

class BillSerializer(serializers.ModelSerializer):

    responsible = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    
    responsible_id = serializers.PrimaryKeyRelatedField(queryset=UserCustomuser.objects.all(), source='responsible', write_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)
    status_id = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all(), source='status', write_only=True)

    class Meta:
        model = Bill
        fields = [
            'id_bill', 'bill_name', 'due_date', 'payday', 'amount',
            'responsible', 'category', 'status',
            'responsible_id', 'category_id', 'status_id'
        ]