import requests
from Secret import APIKEY

class Discount:
    def __init__(self, name, value):
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
        #Valid actions 'Insert', 'Update', 'InsertOrUpdate', 'InsertOrUpdateNonEmptyFields'
        data = {
            "APIKEY": APIKEY,
            "mvDiscount": {
                "DiscountName": self.name,
                "DiscountValue": self.value
            },
            "mvRecordAction": action
        }
        return requests.post('https://api.megaventory.com/v2017a/Discount/DiscountUpdate', json=data)

