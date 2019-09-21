from django.db import models


class StationClass(models.Model):
    name = models.CharField(max_length=32)
    color_name = models.CharField(max_length=32, blank=True)
    color_hex_code = models.CharField(max_length=7, blank=True)
    details = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Station(models.Model):

    dealer = models.ForeignKey("dealers.Dealer", on_delete=models.PROTECT)
    station_class = models.ForeignKey(StationClass, on_delete=models.CASCADE)

    name = models.CharField(max_length=32)
    code = models.CharField(max_length=6, unique=True)
    coordinates = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)
    sub_locality = models.ForeignKey("localities.SubLocality", on_delete=models.CASCADE)
    city = models.CharField(max_length=32, blank=True)
    embed_code = models.TextField(blank=True)
    details = models.TextField(blank=True)
    link = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def get_link(self):
        if self.link:
            return self.link
        else:
            return "-"
