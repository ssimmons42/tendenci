from django import forms
from django.conf import settings

class FirstDataPaymentForm(forms.Form):
    storename = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput, initial=settings.MERCHANT_LOGIN)
    mode = forms.CharField(max_length=7, widget=forms.HiddenInput, initial="payonly")
    txntype = forms.CharField(max_length=4, widget=forms.HiddenInput, initial="sale")
    oid = forms.IntegerField(widget=forms.HiddenInput)
    userid = forms.IntegerField(widget=forms.HiddenInput)
    bcountry = forms.CharField(max_length=60, widget=forms.HiddenInput)
    objectguid = forms.CharField(max_length=100, widget=forms.HiddenInput)
    paymentid = forms.IntegerField(widget=forms.HiddenInput)
    invoiceid = forms.IntegerField(widget=forms.HiddenInput)
    chargetotal = forms.DecimalField(max_digits=15, decimal_places=2, widget=forms.HiddenInput)
    bname = forms.CharField(max_length=100, widget=forms.HiddenInput)
    email = forms.CharField(max_length=255, widget=forms.HiddenInput)
    bcompany = forms.CharField(max_length=50, widget=forms.HiddenInput)
    baddr1 = forms.CharField(max_length=60, widget=forms.HiddenInput)
    baddr2 = forms.CharField(max_length=60, widget=forms.HiddenInput)
    bcity = forms.CharField(max_length=40, widget=forms.HiddenInput)
    bstate = forms.CharField(max_length=40, widget=forms.HiddenInput)
    fax = forms.CharField(max_length=25, widget=forms.HiddenInput)
    phone = forms.CharField(max_length=25, widget=forms.HiddenInput)
    shippingbypass = forms.CharField(max_length=8, widget=forms.HiddenInput, initial="true")
    comments = forms.CharField(max_length=255, required=False, widget=forms.HiddenInput)

