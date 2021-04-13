import requests
from Secret import APIKEY

class SupplierClient:

    def __init__(self, name, email='', shippingAddress='', phone=''):
        self.name = name
        self.email = email
        self.shippingAddress = shippingAddress
        self.phone = phone
    
    def setInfo(self, name=None, email=None, shippingAddress=None, phone=None, post=False):
        self.name = name if name==None else self.name
        self.email = email if email==None else self.email
        self.shippingAddress = shippingAddress if shippingAddress==None else self.shippingAddress
        self.phone = phone if phone==None else self.phone

        if post:
            self(post('Update'))
    
    def getInfo(self):
        return {'Name': self.name,
                'Email': self.email,
                'Shipping Address': self.shippingAddress,
                'Phone': self.phone}

    def post(self, action='InsertOrUpdate'):
        #Valid actions 'Insert', 'Update', 'InsertOrUpdate', 'InsertOrUpdateNonEmptyFields'
        
        data = {
            "APIKEY": APIKEY,
            "mvSupplierClient": {
                "SupplierClientType": "Client",
                "SupplierClientName": self.name,
                "SupplierClientShippingAddress1": self.shippingAddress,
                "SupplierClientPhone1": self.phone,
                "SupplierClientEmail": self.email,
                },
            "mvRecordAction": action,
            }

        return requests.post('https://api.megaventory.com/v2017a/SupplierClient/SupplierClientUpdate', json=data)
    
    def __str__(self):
        return self.getInfo()
