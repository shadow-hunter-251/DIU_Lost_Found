from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from items.models import Item
from notifications.models import Notification

from .forms import ClaimForm
from .models import Claim


@login_required
@require_POST
def claim_action(request, claim_id, action):

    claim = get_object_or_404(
        Claim,
        id=claim_id,
        item__user=request.user
    )

    if claim.status != 'PENDING':

        messages.info(
            request,
            'This claim has already been processed.'
        )

        return redirect(
            'claim_list'
        )

    if action == 'approve':

        claim.status = 'APPROVED'
        claim.save()

        claim.item.status = 'CLAIMED'
        claim.item.save()

        Notification.objects.create(
            user=claim.claimant,
            message=f'Your claim for "{claim.item.title}" has been approved.',
            notification_type='CLAIM_APPROVED'
        )

        messages.success(
            request,
            'Claim approved successfully.'
        )

    elif action == 'reject':

        claim.status = 'REJECTED'
        claim.save()

        Notification.objects.create(
            user=claim.claimant,
            message=f'Your claim for "{claim.item.title}" has been rejected.',
            notification_type='CLAIM_REJECTED'
        )

        messages.success(
            request,
            'Claim rejected successfully.'
        )

    else:

        messages.error(
            request,
            'Invalid claim action.'
        )

    return redirect(
        'claim_list'
    )


@login_required
def submit_claim(request, item_id):

    item = get_object_or_404(
        Item,
        id=item_id,
        item_type='FOUND',
        status='ACTIVE'
    )

    if item.user == request.user:

        messages.error(
            request,
            'You cannot claim your own reported item.'
        )

        return redirect(
            'item_detail',
            item_id=item.id
        )

    existing_claim = Claim.objects.filter(
        item=item,
        claimant=request.user
    ).first()

    if existing_claim:

        messages.info(
            request,
            'You have already submitted a claim for this item.'
        )

        return redirect(
            'item_detail',
            item_id=item.id
        )

    if request.method == 'POST':

        form = ClaimForm(
            request.POST
        )

        if form.is_valid():

            claim = form.save(
                commit=False
            )

            claim.item = item
            claim.claimant = request.user

            claim.save()

            messages.success(
                request,
                'Your claim has been submitted successfully.'
            )

            return redirect(
                'item_detail',
                item_id=item.id
            )

    else:

        form = ClaimForm()

    return render(
        request,
        'claims/submit_claim.html',
        {
            'form': form,
            'item': item,
        }
    )


@login_required
def claim_list(request):

    claims = Claim.objects.filter(
        item__user=request.user
    ).select_related(
        'item',
        'claimant'
    )

    return render(
        request,
        'claims/claim_list.html',
        {
            'claims': claims,
        }
    )