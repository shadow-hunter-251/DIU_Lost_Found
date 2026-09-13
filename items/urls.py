from django.urls import path

from .views import (
    home,
    item_delete,
    item_detail,
    item_edit,
    item_list,
    lost_items,
    found_items,
    report_found,
    report_lost,
)


urlpatterns = [
    path(
        '',
        home,
        name='home'
    ),

    path(
        'items/',
        item_list,
        name='item_list'
    ),

    path(
        'items/<int:item_id>/',
        item_detail,
        name='item_detail'
    ),

    path(
        'items/lost/',
        lost_items,
        name='lost_items'
    ),

    path(
        'items/found/',
        found_items,
        name='found_items'
    ),

    path(
        'items/<int:item_id>/edit/',
        item_edit,
        name='item_edit'
    ),

    path(
        'items/<int:item_id>/delete/',
        item_delete,
        name='item_delete'
    ),

    path(
        'report/lost/',
        report_lost,
        name='report_lost'
    ),

    path(
        'report/found/',
        report_found,
        name='report_found'
    ),
]