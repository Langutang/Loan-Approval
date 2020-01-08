#for the rest_framework
#Handle Requests and converts to JSON files
from rest_framework import serializers
from . models import Approvals

class ApprovalsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Approvals
        fields = '__all__'
