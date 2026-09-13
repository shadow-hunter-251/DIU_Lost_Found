import os

from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from matching.services import find_potential_matches
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from .forms import ItemForm
from .models import Category, Item


def home(request):

    return render(
        request,
        'home.html'
    )


def item_list(request):

    query = request.GET.get(
        'q',
        ''
    ).strip()

    item_type = request.GET.get(
        'type',
        ''
    ).strip()

    category_id = request.GET.get(
        'category',
        ''
    ).strip()

    location = request.GET.get(
        'location',
        ''
    ).strip()


    items = Item.objects.filter(
        status='ACTIVE'
    ).select_related(
        'category',
        'user'
    )


    if query:

        items = items.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(location__icontains=query)
        )


    if item_type in ['LOST', 'FOUND']:

        items = items.filter(
            item_type=item_type
        )


    if category_id:

        items = items.filter(
            category_id=category_id
        )


    if location:

        items = items.filter(
            location__icontains=location
        )


    paginator = Paginator(
        items,
        6
    )


    page_number = request.GET.get(
        'page'
    )


    page_obj = paginator.get_page(
        page_number
    )


    return render(
        request,
        'items/item_list.html',
        {
            'page_obj': page_obj,
            'categories': Category.objects.all(),
            'query': query,
            'item_type': item_type,
            'category_id': category_id,
            'location': location,
        }
    )


def item_detail(request, item_id):

    item = get_object_or_404(
        Item,
        id=item_id
    )


    return render(
        request,
        'items/item_detail.html',
        {
            'item': item,
        }
    )


@login_required
def item_edit(request, item_id):

    item = get_object_or_404(
        Item,
        id=item_id,
        user=request.user
    )


    old_image = item.image


    if request.method == 'POST':

        form = ItemForm(
            request.POST,
            request.FILES,
            instance=item
        )


        if form.is_valid():

            new_image = form.cleaned_data.get(
                'image'
            )


            form.save()


            if new_image and old_image:

                if old_image.name != item.image.name:

                    if os.path.isfile(
                        old_image.path
                    ):

                        os.remove(
                            old_image.path
                        )


            messages.success(
                request,
                'Item updated successfully.'
            )


            return redirect(
                'item_detail',
                item_id=item.id
            )


    else:

        form = ItemForm(
            instance=item
        )


    return render(
        request,
        'items/item_edit.html',
        {
            'form': form,
            'item': item,
        }
    )


@login_required
def item_delete(request, item_id):

    item = get_object_or_404(
        Item,
        id=item_id,
        user=request.user
    )


    if request.method == 'POST':

        item.delete()


        messages.success(
            request,
            'Item deleted successfully.'
        )


        return redirect(
            'item_list'
        )


    return render(
        request,
        'items/item_delete.html',
        {
            'item': item,
        }
    )


def lost_items(request):

    return render(
        request,
        'items/item_list.html',
        {
            'item_filter': 'LOST',
        }
    )


def found_items(request):

    return render(
        request,
        'items/item_list.html',
        {
            'item_filter': 'FOUND',
        }
    )


@login_required
def report_lost(request):

    if request.method == 'POST':

        form = ItemForm(
            request.POST,
            request.FILES
        )


        if form.is_valid():

            item = form.save(
                commit=False
            )


            item.user = request.user

            item.item_type = 'LOST'

            item.save()


            messages.success(
                request,
                'Lost item reported successfully.'
            )


            return redirect(
                'item_list'
            )


    else:

        form = ItemForm()


    return render(
        request,
        'items/report_item.html',
        {
            'form': form,
            'page_title': 'Report Lost Item',
            'button_text': 'Report Lost Item',
        }
    )


@login_required
def report_found(request):

    if request.method == 'POST':

        form = ItemForm(
            request.POST,
            request.FILES
        )


        if form.is_valid():

            item = form.save(
                commit=False
            )


            item.user = request.user

            item.item_type = 'FOUND'

            item.save()


            messages.success(
                request,
                'Found item reported successfully.'
            )


            return redirect(
                'item_list'
            )


    else:

        form = ItemForm()


    return render(
        request,
        'items/report_item.html',
        {
            'form': form,
            'page_title': 'Report Found Item',
            'button_text': 'Report Found Item',
        }
    )
