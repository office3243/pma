from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include("portal.urls", namespace="portal")),
    url(r'^accounts/', include("accounts.urls", namespace="accounts")),
    url(r'^campaigns/', include("campaigns.urls", namespace="campaigns")),
    url(r'^localities/', include("localities.urls", namespace="localities")),
    url(r'^industries/', include("industries.urls", namespace="industries")),
    url(r'^payments/', include("payments.urls", namespace="payments")),
]
