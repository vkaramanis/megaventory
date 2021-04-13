import requests
from Secret import APIKEY

class Product:

    def __init__(self, SKU, description, sales='', purchase=''):
        self.SKU = SKU
        self.description = description
        self.sales = sales
        self.purchase = purchase
    
    def setInfo(self, SKU=None, description=None, sales=None, purchase=None, post=False):
        self.SKU = SKU if SKU==None else self.SKU
        self.description = description if description==None else self.description
        self.sales = sales if sales==None else self.sales
        self.purchase = purchase if purchase==None else self.purchase

        if post:
            self(post('Update'))
    
    def getInfo(self):
        return {'SKU': self.SKU,
                'Description': self.description,
                'Selling Price': self.sales,
                'Purchase Price': self.purchase}

    def post(self, action='InsertOrUpdate'):
        #Valid actions 'Insert', 'Update', 'InsertOrUpdate', 'InsertOrUpdateNonEmptyFields'
        
        data = {
            "APIKEY": APIKEY,
            "mvProduct": {
                "ProductSKU": self.SKU,
                "ProductDescription": self.description,
                "ProductSellingPrice": self.sales,
                "ProductPurchasePrice": self.purchase,
            },
            "mvRecordAction": action
            }
        return requests.post('https://api.megaventory.com/v2017a/Product/ProductUpdate', json=data)
    
    def get(self):
        data = {
            "APIKEY": APIKEY,
            "Filters": [
                {
                "FieldName": "ProductSKU",
                "SearchOperator": "Equals",
                "SearchValue": self.SKU
                }
            ]
            }
        return requests.post('https://api.megaventory.com/v2017a/Product/ProductGet', json=data)

    def __str__(self):
        return self.getInfo()