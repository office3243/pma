from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from . import paytm_checksum as Checksum
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import login
from .models import Payment
from . import alert_messages
from campaigns.models import Campaign
import decimal


@login_required
def create_payment(request, unique_id):
    merchant_key = settings.PAYTM_MERCHANT_KEY
    merchant_id = settings.PAYTM_MERCHANT_ID
    callback_url = settings.PAYTM_CALLBACK_URL
    user = request.user
    campaign = get_object_or_404(Campaign, unique_id=unique_id, user=user)
    if not campaign.is_payed:
        payment = Payment.objects.create(user=user, campaign=campaign, amount=campaign.total_amount)

        data_dict = {
                    'MID': merchant_id,
                    'ORDER_ID': payment.order_id,
                    'TXN_AMOUNT': campaign.total_amount,
                    'CUST_ID': str(user.id),
                    'INDUSTRY_TYPE_ID': 'Retail',
                    'WEBSITE': settings.PAYTM_WEBSITE,
                    'CHANNEL_ID': 'WEB',
                    'CALLBACK_URL': callback_url,
                }
        param_dict = data_dict
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, merchant_key)
        return render(request, "payments/paytm/payment.html", {'paytmdict': param_dict})
    else:
        messages.warning(request, "Campaign amount is already payed!")
        return redirect(campaign.get_absolute_url)


@csrf_exempt
def response(request):
    if request.method == "POST":
        merchant_key = settings.PAYTM_MERCHANT_KEY
        data_dict = {}
        for key in request.POST:
            data_dict[key] = request.POST[key]
        verify = Checksum.verify_checksum(data_dict, merchant_key, data_dict['CHECKSUMHASH'])
        if verify:
            pt_status = data_dict.get("STATUS")
            order_id = data_dict.get("ORDERID")
            amount = decimal.Decimal(data_dict.get("TXNAMOUNT"))
            txnid = data_dict.get("TXNID")
            try:
                payment = Payment.objects.get(order_id=order_id, amount=amount)
                user = payment.user
                if not request.user.is_authenticated:
                    login(request, user)
                campaign = payment.campaign
                if pt_status == "TXN_SUCCESS":
                    payment.status = "SC"
                    payment.txnid = txnid
                    payment.save()
                    campaign.is_payed = True
                    campaign.status = "NA"
                    campaign.save()
                    # campaign.send_email_to_admin()
                    messages.success(request, alert_messages.ORDER_PLACED_MESSAGE)
                    return redirect(campaign.get_absolute_url)
                else:
                    payment.status = "FL"
                    payment.txnid = txnid
                    payment.save()
                    messages.warning(request, alert_messages.PAYMENT_FAILED)
                    return redirect(campaign.get_absolute_url)
            except Payment.DoesNotExist:
                messages.warning(request, alert_messages.PAYMENT_NOT_FOUND)
                return redirect("campaigns:list")
        else:
            return Http404("Payment not verified")
    return Http404("Bad Request")
