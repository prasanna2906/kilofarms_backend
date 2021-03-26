from authenticator.viewsets import RegViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('signup', RegViewset)

