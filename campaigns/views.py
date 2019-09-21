from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Campaign, TestModel
from .forms import CampaignAddForm
from django.urls import reverse_lazy
from django.http import Http404, HttpResponse
import os
from django.views.decorators.csrf import csrf_exempt
from localities.models import State, City, Locality, SubLocality
from industries.models import Category, SubCategory


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

    def form_invalid(self, form):
        print("Form Invalid")
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        print("Form Valid")
        print(self.request.POST, "\n", self.request.FILES)
        form.instance.user = self.request.user
        campaign = form.save()
        return redirect(campaign.get_create_payment_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.filter(is_active=True)
        context['industries'] = Category.objects.filter(is_active=True)
        return context


@csrf_exempt
def campaign_add(request):
    form = CampaignAddForm()
    if request.method == "POST":
        print(request.POST, request.FILES)
    else:
        return render(request, "campaigns/add.html", {'form': form})


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

@csrf_exempt
def blob_test(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        return HttpResponse(request.POST, request.FILES)
    else:
        return render(request, "campaigns/blob_test.html")


class TestCreateView(CreateView):

    model = TestModel
    fields = "__all__"
    template_name = "campaigns/test_create.html"


def test_create(request):
    if request.method == "POST":
        file = request.FILES['myFile']
        TestModel.objects.create(file=file)
    return render(request, "campaigns/test_create.html")