from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Campaign
from .forms import CampaignAddForm
from django.urls import reverse_lazy
from django.http import Http404, HttpResponse
import os


class CampaignListView(LoginRequiredMixin, ListView):
    model = Campaign
    context_object_name = "campaigns"
    template_name = "campaigns/list.html"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class CampaignAddView(LoginRequiredMixin, CreateView):
    form_class = CampaignAddForm
    template_name = "campaigns/add.html"
    success_url = reverse_lazy("campaigns:list")

    def form_valid(self, form):

        form.instance.user = self.request.user
        return super().form_valid(form)


class CampaignDetailView(LoginRequiredMixin, DetailView):

    model = Campaign
    template_name = "campaigns/detail.html"
    slug_field = "unique_id"
    slug_url_kwarg = "unique_id"
    context_object_name = "campaign"

    def get_object(self, queryset=None):
        campaign = super().get_object()
        if campaign.user == self.request.user:
            return campaign
        else:
            raise Http404("No Campaign found with these details.")


def footer_file_download(request, unique_id):
    try:
        file_path = get_object_or_404(Campaign, unique_id=unique_id, user=request.user).footer_file.path
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/pdf")
                response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                return response
        raise Http404
    except Exception as e:
        print(e)
        raise Http404
