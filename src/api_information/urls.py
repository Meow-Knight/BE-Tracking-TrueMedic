from rest_framework import routers

from api_information.views import AgentViewSet, MedicineViewSet, MedicineUnitViewSet, ProducerViewSet, ShipmentViewSet

app_name = 'api_information'
router = routers.SimpleRouter(trailing_slash=True)
router.register(r'agent', AgentViewSet, basename='agent')
router.register(r'medicine', MedicineViewSet, basename='medicine')
router.register(r'medicine_unit', MedicineUnitViewSet, basename='medicine_unit')
router.register(r'producer', ProducerViewSet, basename='producer')
router.register(r'shipment', ShipmentViewSet, basename='shipment')

urlpatterns = router.urls
