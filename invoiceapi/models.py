# invoice_app/models.py
from django.db import models

class Invoice(models.Model):
    date = models.DateField(auto_now=True)
    CustomerName = models.CharField(max_length=100)

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice_details')
    description = models.CharField(max_length=255,null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.invoice.id} - {self.description}"
