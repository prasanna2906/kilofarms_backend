from django.urls import path
from . import views

urlpatterns = [
    path('', views.Productview,name = "product-views"),
    path('listprods/',views.productList, name = "listprods"),
    path('product_details/<str:pk>/',views.productDetail, name="product-details"),
    path('createSKU/',views.productCreate, name = "create-prods"),
    path('product_update/<str:pk>/',views.productUpdate, name = "update-prods"),
    path('product_del/<str:pk>/',views.productDelete, name = "delete-prods")
]