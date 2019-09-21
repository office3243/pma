from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .models import Station
from io import StringIO, BytesIO
from zipfile import ZipFile
from django.http import HttpResponse
import os
from django.http import Http404


class StationListView(LoginRequiredMixin, ListView):
    model = Station
    template_name = "stations/list.html"
    context_object_name = "stations"
    # paginate_by = 10


def get_footer_files(request):
    if request.method == "POST":

        pages = int(request.POST['no_of_pages'])
        station_code = request.POST['station_code']
        try:
            station_active_campaigns = request.POST['station_active_campaigns'].split(",")
        except:
            station_active_campaigns = []
        station = get_object_or_404(Station, code=station_code)
        campaigns = station.sub_locality.campaign_set.filter(is_active=True, is_finished=False,
                                                             status="RN")  # status is VIMP
        print(campaigns)
        equal_copies = pages // campaigns.count()
        non_equal_copies = equal_copies + (pages % campaigns.count())
        for i, campaign in enumerate(campaigns):
            if i == 0:
                difference_of_copies = campaign.get_prints(non_equal_copies)
            else:
                difference_of_copies = campaign.get_prints(equal_copies)
            if difference_of_copies > 0:
                non_equal_copies += difference_of_copies
        station_need_campaigns = campaigns.exclude(unique_id__in=station_active_campaigns)
        footer_files = [campaign.footer_file for campaign in station_need_campaigns]

        in_memory = BytesIO()
        zip_file = ZipFile(in_memory, "a")

        for footer_file in footer_files:
            zip_file.writestr(os.path.basename(footer_file.name), footer_file.read())

        # fix for Linux zip files read in Windows
        for file in zip_file.filelist:
            file.create_system = 0

        zip_file.close()

        response = HttpResponse(content_type="application/zip")
        response['active_campaigns'] = campaigns
        response['campaigns_sent'] = station_need_campaigns
        response["Content-Disposition"] = "attachment; filename=recent_campaigns.zip"
        in_memory.seek(0)
        response.write(in_memory.read())

        return response
    raise Http404("Bad Request")
