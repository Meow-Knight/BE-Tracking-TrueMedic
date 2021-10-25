from rest_framework import routers

from api_garden.views import PlantViewSet, UserViewSet, FavouritePlantViewSet


app_name = 'api_garden'
router = routers.SimpleRouter(trailing_slash=True)
router.register(r'plant', PlantViewSet, basename='plants')
router.register(r'user', UserViewSet, basename='users')
router.register(r'favourite_plant', FavouritePlantViewSet, basename='favourite_plants')

urlpatterns = router.urls
