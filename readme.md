# Invoice Management Application

This is a Django Rest Framework (DRF) application for managing invoices and their details. The application provides APIs for creating, retrieving, updating, and deleting invoices along with their associated invoice details.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)

## Installation

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/kiranrokkam09/Invoice_Management.git
   cd Invoice_Management
   ```

2. Set up a virtual environment and install the dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the database migrations and create a superuser:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

## Usage

To start the Django development server, run the following command:

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`. You can access the Django admin panel at `http://127.0.0.1:8000/admin/` and use the superuser credentials to log in.

## API Endpoints

The application provides the following API endpoints:

- **POST /api/invoices/**: Create a new invoice along with its associated invoice details. The payload should include the invoice details as a nested array.
example:
         {
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
- **GET /api/invoices/{invoice_id}/**: Retrieve details of a specific invoice.
- **PUT /api/invoices/{invoice_id}/**: Update details of a specific invoice.

Note: For the POST and PUT requests, the payload should be in JSON format.

## Testing

   For testing the api end points you can use the command.

      ```bash
         python manage.py test
      ```
