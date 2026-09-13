from django import forms

from .models import Item
from django.utils import timezone


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = [
            'title',
            'category',
            'description',
            'location',
            'date',
            'image',
        ]

    def clean_date(self):
        date = self.cleaned_data.get('date')

        if date and date > timezone.now().date():
            raise forms.ValidationError(
                'Date cannot be in the future.'
            )

        return date

    def clean_title(self):

        title = self.cleaned_data.get('title')

        if title and len(title.strip()) < 3:
            raise forms.ValidationError(
                'Title must contain at least 3 characters.'
            )

        return title.strip()

    def clean_description(self):

        description = self.cleaned_data.get(
            'description'
        )

        if description and len(description.strip()) < 10:
            raise forms.ValidationError(
                'Description must contain at least 10 characters.'
            )

        return description.strip()

    def clean_location(self):

        location = self.cleaned_data.get(
            'location'
        )

        if location and len(location.strip()) < 3:
            raise forms.ValidationError(
                'Location must contain at least 3 characters.'
            )

        return location.strip()

    def clean_image(self):

        image = self.cleaned_data.get('image')

        if not image:
            return image

        if image.size > 5 * 1024 * 1024:
            raise forms.ValidationError(
                'Image size must be less than 5 MB.'
            )

        allowed_types = [
            'image/jpeg',
            'image/png',
            'image/webp',
        ]

        if image.content_type not in allowed_types:
            raise forms.ValidationError(
                'Only JPG, PNG, and WEBP images are allowed.'
            )

        return image