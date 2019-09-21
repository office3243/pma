from django.conf.urls import url
from . import views

app_name = 'stations'


urlpatterns = [
    url(r'^list/$', views.StationListView.as_view(), name="list"),
    url(r"^get_footer_files/(?P<station_code>[0-9a-zA-Z-]+)/(?P<pages>[0-9]+)$", views.get_footer_files,
        name="get_footer_files"),

]
