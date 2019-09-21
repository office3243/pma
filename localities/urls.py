from django.conf.urls import url
from . import views

app_name = "localities"

urlpatterns = [
    # url(r"^get_footer_files/(?P<station_code>[0-9a-zA-Z-]+)/(?P<pages>[0-9]+)$", views.get_footer_files, name="get_footer_files"),
    url(r"^get_footer_files/$", views.get_footer_files, name="get_footer_files"),

]
