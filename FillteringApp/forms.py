from django import forms
from .models import Review

# class MyForm(forms.Form):
#     my_field = forms.ModelChoiceField(
#         queryset=Review.objects.values_list('rating', flat=True).distinct(),
#         empty_label=None,
#         widget=forms.Select(attrs={'class': 'form-control'})
#     )

