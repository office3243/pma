from django import forms
from .models import Campaign


class CampaignAddForm(forms.ModelForm):

    class Meta:
        model = Campaign
        fields = ("name", "size", "footer_file", "sub_industry", "sub_locality", "quantity")
