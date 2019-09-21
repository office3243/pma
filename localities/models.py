from django.db import models


class State(models.Model):
    name = models.CharField(max_length=64)
    attr_name = models.CharField(max_length=6, blank=True)
    extra_info = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def get_active_cities(self):
        return self.city_set.filter(is_active=True)

    @property
    def get_display_text(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=64)
    attr_name = models.CharField(max_length=6, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    extra_info = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def get_active_localities(self):
        return self.locality_set.filter(is_active=True)

    @property
    def get_display_text(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"


class Locality(models.Model):

    name = models.CharField(max_length=64)
    attr_name = models.CharField(max_length=6, blank=True)
    postal_code = models.CharField(max_length=6)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    extra_info = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def get_active_sub_localities(self):
        return self.sublocality_set.filter(is_active=True)

    @property
    def get_display_text(self):
        return self.name

    class Meta:
        verbose_name_plural = "Localities"


class SubLocality(models.Model):

    name = models.CharField(max_length=64)
    attr_name = models.CharField(max_length=6, blank=True)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE)
    extra_info = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def get_display_text(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sub Localities"
