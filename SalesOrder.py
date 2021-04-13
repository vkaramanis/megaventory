import requests
from Secret import APIKEY

class SalesOrder:
    def __init__(self, product, client):
        self.name = name
        self.value = value
    
    def updateInfo(self, name=None, value=None, post=False):
        self.name = name if name==None else self.name
        self.value = value if value==None else self.value

        if post:
            self(post('Update'))
    
    def getInfo(self):
        return {'Name': self.name,
                'Value': self.value}

    def post(self, action='InsertOrUpdate'):
        # Valid actions  'Insert'. 'Update', 'InsertOrUpdate'. 'InsertOrUpdateNonEmptyFields'.
        # 'Save'. 'SaveNonEmptyFields', 'Verify', 'RevertToPending', 'Close', 'ReOpen', 'Cancel',
        # 'Delete', 'Clone', 'ReceiveItems', 'ShipItems', 'InvoiceItems'
        data = {
            'APIKEY': APIKEY,
            "mvSalesOrder": {
                "SalesOrderTypeId": "84",
                "SalesOrderClientId": 5358,
                'SalesOrderShippingAddress':'',
                "SalesOrderInventoryLocationID": 4430,
                "SalesOrderTotalQuantity": "",
                "SalesOrderAmountSubtotalWithoutTaxAndDiscount": '',
                "SalesOrderAmountShipping": "",
                "SalesOrderAmountTotalDiscount": "",
                "SalesOrderAmountTotalTax": "",
                "SalesOrderAmountGrandTotal": "",
                "SalesOrderDetails": [
                {
                    "SalesOrderRowProductSKU": "product",
                    "SalesOrderRowQuantity": "10",
                    "SalesOrderRowShippedQuantity": "2",
                    "SalesOrderRowInvoicedQuantity": "2",
                    "SalesOrderRowUnitPriceWithoutTaxOrDiscount": "0.93",
                    'SalesOrderRowTaxID': '',
                    'SalesOrderTotalTaxAmount': '',
                    'SalesOrderRowDiscountID': '',
                    'SalesOrderRowTotalDiscountAmount': '',
                    'SalesOrderRowTotalAmount': '',
                }
                ],
                "SalesOrderShipDocumentTypeID": 2,
                "SalesOrderStatus": "PartiallyShippedAndPartiallyInvoiced"
            },
            "mvRecordAction": action
        }
        return requests.post('https://api.megaventory.com/v2017a/Tax/TaxUpdate', json=data)