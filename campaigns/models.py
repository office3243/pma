from django.db import models
from django.db.models.signals import pre_delete, pre_save, post_save
import decimal
import random
import string
from django.urls import reverse_lazy
from django.conf import settings
from django.core.validators import FileExtensionValidator
from rates.models import QuantityRate
from django.core.mail import send_mail


class Entity(models.Model):
    FONT_CHOICES = (("AR", "Arial"), ("CL", "Calibari"), ("HL", "Halvetica"), ("TR", "Times Roman"))

    name = models.CharField(max_length=32)
    default_font = models.CharField(max_length=4, choices=FONT_CHOICES, blank=True)
    default_font_size = models.CharField(max_length=32, blank=True)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Entities"


class Size(models.Model):
    name = models.CharField(max_length=64)
    length = models.CharField(max_length=32)
    height = models.CharField(max_length=32)
    entities = models.ManyToManyField(Entity)

    def __str__(self):
        return self.name


def unique_id_generator(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    random_id = ''.join(random.choice(chars) for _ in range(size))
    if not Campaign.objects.filter(unique_id=random_id).exists():
        return random_id
    return unique_id_generator()


class Campaign(models.Model):
    STATUS_CHOICES = (("PP", "Payment Pending"), ("DC", "Declined"), ("NA", "Not Approved"), ("AP", "Approved"),
                      ("RN", "Running"), ("FN", "Finished"), ("CN", "Cancelled"))

    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=64, blank=True, default=unique_id_generator)
    name = models.CharField(max_length=64, blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    footer_file = models.FileField(upload_to="campaigns/footer_files/",
                                   validators=[FileExtensionValidator(allowed_extensions=("pdf", )), ])
    sub_industry = models.ForeignKey("industries.SubCategory", on_delete=models.PROTECT)
    sub_locality = models.ForeignKey("localities.SubLocality", on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=100)
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    extra_charges = models.DecimalField(help_text="GST and other charges", max_digits=8, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    printed_copies = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="PP")

    is_finished = models.BooleanField(default=False)
    is_payed = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or str(self.created_on)

    @property
    def calculate_amount(self):
        rate = QuantityRate.objects.filter(is_active=True, min_quantity__lte=self.quantity).order_by("min_quantity").first()
        amount = self.quantity * rate.amount_per_unit
        return amount

    @property
    def get_create_payment_url(self):
        return reverse_lazy("payments:create_payment", kwargs={'unique_id': self.unique_id})

    @property
    def get_display_text(self):
        return self.name

    @property
    def get_absolute_url(self):
        return reverse_lazy("campaigns:detail", kwargs={'unique_id': self.unique_id})

    @property
    def get_footer_file_download_related_url(self):
        return reverse_lazy("campaigns:footer_file_download", kwargs={'unique_id': self.unique_id})

    @property
    def get_footer_file_download_absolute_url(self):
        return settings.SITE_DOMAIN + str(reverse_lazy("campaigns:footer_file_download",
                                                       kwargs={'unique_id': self.unique_id}))

    @property
    def get_remaining_copies(self):
        return self.quantity - self.printed_copies

    def get_prints(self, copies):
        remaining_copies = self.get_remaining_copies
        difference = copies - remaining_copies
        if difference <= 0:
            add_copies = copies
        else:
            add_copies = remaining_copies
        self.printed_copies += add_copies
        self.save()
        return difference

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        """Check the total files printed and assign finished status"""
        if self.quantity <= self.printed_copies:
            self.is_finished = True
            self.status = "FN"
        super().save()


def assign_amount(sender, instance, *args, **kwargs):
    amount = instance.calculate_amount
    if instance.amount != amount:
        instance.amount = instance.calculate_amount
        instance.save()
    if instance.amount and not instance.extra_charges:
        extra_charges = decimal.Decimal(float(instance.amount) * 0.18)
        if instance.extra_charges != extra_charges:
            instance.extra_charges = extra_charges
            instance.total_amount = instance.amount + instance.extra_charges
            instance.save()
    total_amount = instance.amount + instance.extra_charges
    if instance.total_amount != total_amount:
        instance.total_amount = total_amount
        instance.save()


def add_campaign_name(sender, instance, *args, **kwargs):
    if not instance.name and instance.user:
        name = "Campaign " + str(instance.user.campaign_set.count())
        instance.name = name
        instance.save()


pre_save.connect(assign_amount, Campaign)
post_save.connect(add_campaign_name, sender=Campaign)


class TestModel(models.Model):

    file = models.FileField(upload_to="campaigns/test_models/")
    text = models.TextField(blank=True)


    def __str__(self):
        return str(self.id)

