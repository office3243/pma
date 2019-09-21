from django.db import models
import random
import string


def order_id_generator(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    random_id = ''.join(random.choice(chars) for _ in range(size))
    if not Payment.objects.filter(order_id=random_id).exists():
        return random_id
    return order_id_generator()


class Payment(models.Model):

    STATUS_CHOICES = (('IN', "Initiated"), ("SC", "Success"), ("FL", "Failed"))

    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    order_id = models.CharField(max_length=64, default=order_id_generator)
    txnind = models.CharField(max_length=64, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="IN")

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.user, self.amount)

