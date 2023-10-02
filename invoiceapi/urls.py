# invoice_app/urls.py
from django.urls import path
from .views import InvoiceView,SingleInvoiceView,index

urlpatterns = [
    path('',index),
    path('invoices/', InvoiceView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', SingleInvoiceView.as_view(), name='invoice-retrieve-update-destroy'),
]
