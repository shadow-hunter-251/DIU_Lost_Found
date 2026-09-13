from django.urls import path

from .views import (
    admin_dashboard,
    dashboard_home,
)


urlpatterns = [
    path(
        '',
        dashboard_home,
        name='dashboard'
    ),

    path(
        'admin-dashboard/',
        admin_dashboard,
        name='admin_dashboard'
    ),
]