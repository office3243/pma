from django.db import models


class State(models.Model):
    name = models.CharField(max_length=64)
    short_name = models.CharField(max_length=6, blank=True)
    extra_info = models.TextField(blank=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=64)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    extra_info = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"


class Locality(models.Model):
    name = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=6)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    extra_info = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Localities"
