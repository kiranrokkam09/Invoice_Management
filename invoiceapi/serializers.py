# invoice_app/serializers.py
from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['description','quantity','unit_price','price']

class InvoiceSerializer(serializers.ModelSerializer):
    invoice_details = InvoiceDetailSerializer(many=True,required=False)
    class Meta:
        model = Invoice
        fields = ['CustomerName','invoice_details']
