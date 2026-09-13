from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from claims.models import Claim
from items.models import Item


@login_required
def dashboard_home(request):

    items = Item.objects.filter(
        user=request.user
    )

    total_items = items.count()

    lost_items = items.filter(
        item_type='LOST'
    ).count()

    found_items = items.filter(
        item_type='FOUND'
    ).count()

    active_items = items.filter(
        status='ACTIVE'
    ).count()

    return render(request, 'dashboard/dashboard.html', {
        'items': items,
        'total_items': total_items,
        'lost_items': lost_items,
        'found_items': found_items,
        'active_items': active_items,
    })


@login_required
def admin_dashboard(request):

    if not request.user.is_staff:
        return render(
            request,
            'dashboard/access_denied.html',
            status=403
        )

    total_users = User.objects.count()

    total_items = Item.objects.count()

    lost_items = Item.objects.filter(
        item_type='LOST'
    ).count()

    found_items = Item.objects.filter(
        item_type='FOUND'
    ).count()

    active_items = Item.objects.filter(
        status='ACTIVE'
    ).count()

    claimed_items = Item.objects.filter(
        status='CLAIMED'
    ).count()

    total_claims = Claim.objects.count()

    pending_claims = Claim.objects.filter(
        status='PENDING'
    ).count()

    recent_users = User.objects.order_by(
        '-date_joined'
    )[:5]

    recent_items = Item.objects.select_related(
        'user',
        'category'
    ).order_by(
        '-created_at'
    )[:5]

    recent_claims = Claim.objects.select_related(
        'item',
        'claimant'
    ).order_by(
        '-created_at'
    )[:5]

    return render(
        request,
        'dashboard/admin_dashboard.html',
        {
            'total_users': total_users,
            'total_items': total_items,
            'lost_items': lost_items,
            'found_items': found_items,
            'active_items': active_items,
            'claimed_items': claimed_items,
            'total_claims': total_claims,
            'pending_claims': pending_claims,
            'recent_users': recent_users,
            'recent_items': recent_items,
            'recent_claims': recent_claims,
        }
    )