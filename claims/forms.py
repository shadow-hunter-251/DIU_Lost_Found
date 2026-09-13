from django import forms

from .models import Claim


class ClaimForm(forms.ModelForm):

    class Meta:
        model = Claim

        fields = [
            'message',
        ]

        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'w-full border border-slate-300 rounded-lg px-4 py-3',
                'rows': 6,
                'placeholder': 'Explain why this item belongs to you...'
            }),
        }