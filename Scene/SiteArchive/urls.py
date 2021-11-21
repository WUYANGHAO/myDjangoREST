from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('sites',SiteViewSet)
router.register('networkings',NetworkingViewSet)
router.register('features',FeatureViewSet)
router.register('operations',OperationViewSet)
router.register('operateroles',OperateroleViewSet)
router.register('operatedetails',OperatedetailViewSet)
router.register('requires',RequireViewSet)
router.register('onlineissues',OnlineissueViewSet)
router.register('travelreports',TravelreportViewSet)

urlpatterns = []
urlpatterns+=router.urls