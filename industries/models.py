from django.db import models


class Category(models.Model):

    POPULARITY_CHOICES = (("LT", "Lowest"), ("LW", "Low"), ("MD", "Medium"), ("HI", "High"), ("HT", "Highest"))

    name = models.CharField(max_length=64)
    attr_name = models.CharField(max_length=6, blank=True)
    rate_ratio = models.FloatField(default=1.1)
    popularity = models.CharField(max_length=2, choices=POPULARITY_CHOICES, default="MD")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def get_active_sub_categories(self):
        return self.subcategory_set.filter(is_active=True)

    @property
    def get_display_text(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class SubCategory(models.Model):

    name = models.CharField(max_length=64)
    attr_name = models.CharField(max_length=6, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def get_display_text(self):
        return self.name

    class Meta:
        verbose_name_plural = "Sub Categories"
