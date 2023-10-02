from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail

class InvoiceViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_invoice(self):
        # Define the data to create a new invoice
        data = {
            "CustomerName": "John Doe",
            "invoice_details": [
                {
                    "description": "Item 1",
                    "quantity": 2,
                    "unit_price": 10.0,
                    "price": 20.0
                },
                {
                    "description": "Item 2",
                    "quantity": 1,
                    "unit_price": 15.0,
                    "price": 15.0
                }
            ]
        }

        response = self.client.post('/invoices/', data, format='json')

        # Check if the response status code is 201 (created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the invoice was created in the database
        self.assertEqual(Invoice.objects.count(), 1)

        # Check if the invoice details were created in the database
        self.assertEqual(InvoiceDetail.objects.count(), 2)

    # You can write more tests for different scenarios, such as validation errors, etc.

class SingleInvoiceViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_update_invoice(self):
        # Create an initial invoice and associated details
        invoice = Invoice.objects.create(CustomerName="John Doe")
        InvoiceDetail.objects.create(
            invoice=invoice,
            description="Item 1",
            quantity=2,
            unit_price=10.0,
            price=20.0
        )
        InvoiceDetail.objects.create(
            invoice=invoice,
            description="Item 2",
            quantity=1,
            unit_price=15.0,
            price=15.0
        )

        # Define the data to update the invoice
        data = {
            "CustomerName": "Jane Smith",
            "invoice_details": [
                {
                    "description": "Updated Item 1",
                    "quantity": 3,
                    "unit_price": 12.0,
                    "price": 36.0
                },
                {
                    "description": "New Item",
                    "quantity": 4,
                    "unit_price": 8.0,
                    "price": 32.0
                }
            ]
        }

        response = self.client.put(f'/invoices/{invoice.id}/', data, format='json')

        # Check if the response status code is 201 (created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the invoice details were updated in the database
        self.assertEqual(len(response.data['New Data']['invoice_details']), 2)

        # Check if the invoice's customer name was updated
        updated_invoice = Invoice.objects.get(id=invoice.id)
        self.assertEqual(response.data['New Data']['CustomerName'], "Jane Smith")

    # You can write more tests for different scenarios, such as partial updates, validation errors, etc.
