from django.conf.urls import url
from . import views

app_name = "payments"

urlpatterns = [
    url(r'^create_payment/(?P<unique_id>[0-9a-zA-Z-]+)/$', views.create_payment, name="create_payment")

]