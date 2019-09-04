from django.db import models


class Category(models.Model):

    POPULARITY_CHOICES = (("LT", "Lowest"), ("LW", "Low"), ("MD", "Medium"), ("HI", "High"), ("HT", "Highest"))

    name = models.CharField(max_length=64)
    rate_ratio = models.FloatField(default=1.1)
    popularity = models.CharField(max_length=2, choices=POPULARITY_CHOICES, default="MD")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class SubCategory(models.Model):

    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sub Categories"
