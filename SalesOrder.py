import requests
from Secret import APIKEY
import itertools

class SalesOrder:
    id_iter = itertools.count()
    def __init__(self, productSKU, quantity, price, clientId, warehouseId, tax, discount, status):
        self.id = next(SalesOrder.id_iter)
        self.productSKU = productSKU
        self.quantity = quantity
        self.price = price
        self.clientId = clientId
        self.warehouseId = warehouseId
        self.tax = tax
        self.discount = discount
        self.totalWithoutTaxandDiscount = self.quantity * self.price
        self.totalDiscount = self.totalWithoutTaxandDiscount * self.discount
        self.totalTax = (self.totalWithoutTaxandDiscount - self.discount) * self.tax
        self.grandTotal = self.totalWithoutTaxandDiscount - self.totalDiscount + self.totalTax
        self.status = status
    
    def updateInfo(self, productSKU=None, quantity=None, price=False, clientId=None, warehouseId=None, tax=False, discount=None, post=False):
        self.productSKU = productSKU if productSKU==None else self.productSKU
        self.quantity = quantity if quantity==None else self.quantity
        self.price = price if price==None else self.price
        self.clientId = clientId if clientId==None else self.clientId
        self.warehouseId = warehouseId if warehouseId==None else self.warehouseId
        self.tax = tax if tax==None else self.tax
        self.discount = discount if discount==None else self.discount

        if post:
            self(post('Update'))
    
    def get(self):
        data = {
            "APIKEY": APIKEY,
            "Filters": [
                {
                "FieldName": "SalesOrderTypeId",
                "SearchOperator": "Equals",
                "SearchValue": self.id
                }
            ]
            }
        return requests.post('https://api.megaventory.com/v2017a/SalesOrder/SalesOrderGet', json=data)

    def post(self, action='InsertOrUpdate'):
        # Valid actions  'Insert'. 'Update', 'InsertOrUpdate'. 'InsertOrUpdateNonEmptyFields'.
        # 'Save'. 'SaveNonEmptyFields', 'Verify', 'RevertToPending', 'Close', 'ReOpen', 'Cancel',
        # 'Delete', 'Clone', 'ReceiveItems', 'ShipItems', 'InvoiceItems'
        data = {
            'APIKEY': APIKEY,
            "mvSalesOrder": {
                "SalesOrderTypeId": self.id,
                "SalesOrderClientId": self.clientId,
                "SalesOrderInventoryLocationID": self.warehouseId,
                "SalesOrderTotalQuantity":  self.quantity,
                "SalesOrderAmountSubtotalWithoutTaxAndDiscount":  self.totalWithoutTaxandDiscount,
                "SalesOrderAmountTotalDiscount": self.totalDiscount,
                "SalesOrderAmountTotalTax": self.totalTax,
                "SalesOrderAmountGrandTotal": self.grandTotal,
                'SalesOrderStatus': self.status,
                "SalesOrderDetails": [
                    {
                    "SalesOrderRowProductSKU": self.productSKU,
                    "SalesOrderRowQuantity": self.quantity,
                    "SalesOrderRowShippedQuantity": self.quantity,
                    "SalesOrderRowInvoicedQuantity": self.quantity,
                    "SalesOrderRowUnitPriceWithoutTaxOrDiscount": self.price,
                    'SalesOrderTotalTaxAmount': self.tax,
                    'SalesOrderRowTotalDiscountAmount': self.discount,
                    'SalesOrderRowTotalAmount': self.grandTotal,
                    }
                ],
            },
            "mvRecordAction": action
        }
        return requests.post('https://api.megaventory.com/v2017a/SalesOrder/SalesOrderUpdate', json=data)