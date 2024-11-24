# forms.py
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['pengguna', 'rating', 'komentar']
        widgets = {
            'komentar': forms.Textarea(attrs={'rows': 4}),
        }
