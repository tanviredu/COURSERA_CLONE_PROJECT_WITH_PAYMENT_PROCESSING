from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

from .models import BillingAddress
from .forms import BillingForm

from App_Order.models import Order,Cart

from django.contrib.auth.decorators import login_required


@login_required
def checkout(request):
    ## get the billing address object or if not then
    ## create a empty Billing Address object with the user instance 