from django.urls import path

from .views import (
    claim_action,
    claim_list,
    submit_claim,
)


urlpatterns = [
    path(
        'item/<int:item_id>/claim/',
        submit_claim,
        name='submit_claim'
    ),

    path(
        '',
        claim_list,
        name='claim_list'
    ),

    path(
        '<int:claim_id>/<str:action>/',
        claim_action,
        name='claim_action'
    ),
]