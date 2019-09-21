from django.db import models


class Rate(models.Model):
    sub_industry = models.ForeignKey("industries.SubCategory", on_delete=models.CASCADE)
    industry = models.ForeignKey("industries.Category", on_delete=models.CASCADE)
    locality = models.ForeignKey("localities.Locality", on_delete=models.CASCADE)
    city = models.ForeignKey("localities.City", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)


class QuantityRate(models.Model):

    min_quantity = models.PositiveIntegerField(default=1)
    amount_per_unit = models.DecimalField(max_digits=6, decimal_places=2)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{} Rs (min quantity {})".format(self.amount_per_unit, self.min_quantity)
