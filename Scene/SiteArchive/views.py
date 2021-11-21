from rest_framework import pagination, viewsets
from .serializers import *
from .models import *
from .pagination import StandardPageNumberPagination

class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    filter_fields = ['site_name']
    pagination_class = StandardPageNumberPagination

class NetworkingViewSet(viewsets.ModelViewSet):
    queryset = Networking.objects.all()
    serializer_class = NetworkingSerializer

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer

class OperateroleViewSet(viewsets.ModelViewSet):
    queryset = Operaterole.objects.all()
    serializer_class = OperateroleSerializer

class OperatedetailViewSet(viewsets.ModelViewSet):
    queryset = Operatedetail.objects.all()
    serializer_class = OperatedetailSerializer

class RequireViewSet(viewsets.ModelViewSet):
    queryset = Require.objects.all()
    serializer_class = RequireSerializer

class OnlineissueViewSet(viewsets.ModelViewSet):
    queryset = Onlineissue.objects.all()
    serializer_class = OnlineissueSerializer

class TravelreportViewSet(viewsets.ModelViewSet):
    queryset = Travelreport.objects.all()
    serializer_class = TravelreportSerializer