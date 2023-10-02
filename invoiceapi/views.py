# invoice_app/views.py
from rest_framework import generics
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

# View to display a welcome message
def index(request):
    return HttpResponse("Hello Invoice API!")

# View to create a new invoice
class InvoiceView(generics.CreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def post(self, request):
        # Get the invoice details from the request data
        details = request.data.get('invoice_details')

        # Create a new invoice with the customer name
        invoice = Invoice.objects.create(CustomerName=request.data['CustomerName'])
        invoice.save()

        # Create invoice details for each item in the details list
        for detail in details:
            invoiceDetail = InvoiceDetail.objects.create(
                invoice=invoice,
                description=detail['description'],
                quantity=detail['quantity'],
                unit_price=detail['unit_price'],
                price=detail['price']
            )
            invoiceDetail.save()

        # Return a success response
        return Response({"message": "Invoice Created", "id": invoice.id}, status=status.HTTP_201_CREATED)

# View to retrieve and update a single invoice
class SingleInvoiceView(generics.RetrieveUpdateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def update(self, request, pk):
        # Create a serializer instance and validate the incoming data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Retrieve the existing Invoice instance
        invoice = Invoice.objects.get(id=pk)
        
        # Retrieve the associated invoice details
        invoicedetail = InvoiceDetail.objects.filter(invoice=invoice)
        
        # Update the invoice customer name if it has changed
        if invoice.CustomerName != request.data['CustomerName']:
            invoice = Invoice.objects.create(CustomerName=request.data['CustomerName'])
        
        # Create a list to keep track of updated invoice detail IDs
        idlst = []

        # Iterate through the changed details and update the corresponding invoice details
        i = 0
        changeddetails = request.data['invoice_details']
        for detail in changeddetails:
            try:
                instance = InvoiceDetail.objects.get(id=idlst[i])
                i += 1         
                instance.invoice = invoice
                instance.description = detail['description']
                instance.quantity = detail['quantity']
                instance.unit_price = detail['unit_price']
                instance.price = detail['price']
                instance.save()
            except IndexError:
                InvoiceDetail.objects.create(
                invoice=invoice,
                description=detail['description'],
                quantity=detail['quantity'],
                unit_price=detail['unit_price'],
                price=detail['price']
            )

        
        # Prepare the response data
        data = {
            "Message": "Data Updated",
            "New Data": request.data
        }
        return Response(data, status=status.HTTP_201_CREATED)
    
    def patch(self, request, pk):
        # Delegate to the update method and return the same response
        self.update(request, pk)
        data = {
            "Message": "Data Updated",
            "New Data": request.data
        }
        return Response(data, status=status.HTTP_201_CREATED)
