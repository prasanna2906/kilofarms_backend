from prod.viewsets import ProductViewset, ProductGetViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('createSKU', ProductViewset)
router.register('prodid', ProductGetViewset, basename='ProductGet')
router.register('del', ProductViewset)
router.register('product?id=3', ProductViewset)
