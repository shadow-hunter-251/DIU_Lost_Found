from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    ItemDetailAPIView,
    ItemListAPIView,
)

urlpatterns = [

    path(
        'token/',
        obtain_auth_token,
        name='api_token'
    ),

    path(
        'items/',
        ItemListAPIView.as_view(),
        name='api_item_list'
    ),

    path(
        'items/<int:item_id>/',
        ItemDetailAPIView.as_view(),
        name='api_item_detail'
    ),

]