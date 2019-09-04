from django.db import models


class Payment(models.Model):

    STATUS_CHOICES = (('IN', "Initiated"), ("SC", "Success"), ("FL", "Failed"))

    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    order_id = models.CharField(max_length=64)
    txnind = models.CharField(max_length=64)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.user, self.amount)

