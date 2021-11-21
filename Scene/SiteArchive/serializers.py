from django.db.models import fields
from django.utils.translation import activate
from rest_framework import serializers
from .models import *

class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'

class NetworkingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Networking
        fields = '__all__'

class FeatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

class OperationSerializer(serializers.HyperlinkedModelSerializer):
    operaterole_set = serializers.StringRelatedField(many=True)
    operatedetail_set = serializers.StringRelatedField(many=True)
    class Meta:
        model = Operation
        fields = '__all__'

class OperateroleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operaterole
        fields = '__all__'

class OperatedetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operatedetail
        fields = '__all__'

class RequireSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Require
        fields = '__all__'

class OnlineissueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Onlineissue
        fields = '__all__'

class TravelreportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Travelreport
        fields = '__all__'