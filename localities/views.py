from django.shortcuts import render, get_object_or_404
from .models import Locality, SubLocality
from campaigns.models import Campaign
from stations.models import Station


def get_footer_files(request, station_code, pages):
    station = get_object_or_404(Station, station_code=station_code)
    campaigns = station.sub_locality.campaign_set.filter(is_active=True, is_finished=False,
                                                         status="RN")  # status is VIMP

    footer_files = [campaign.footer_file for campaign in campaigns]
