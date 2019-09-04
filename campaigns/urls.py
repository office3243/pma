from django.conf.urls import url
from . import views

app_name = "campaigns"

urlpatterns = [
    url(r"^list/$", views.CampaignListView.as_view(), name="list"),
    url(r"^add/$", views.CampaignAddView.as_view(), name="add"),
    url(r"^detail/(?P<unique_id>[0-9a-zA-Z-]+)/$", views.CampaignDetailView.as_view(), name="detail"),
    url(r"^footer_file/download/(?P<unique_id>[0-9a-zA-Z-]+)/$", views.footer_file_download, name="footer_file_download"),

]
