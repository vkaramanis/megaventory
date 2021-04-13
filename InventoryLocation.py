import requests
from Secret import APIKEY

class InventoryLocation:
    def __init__(self, abbreviation, name, address=''):
        self.abbreviation = abbreviation
        self.name = name
        self.address = address
    
    def setInfo(self, abbreviation=None, name=None, address=None, post=False):
        self.abbreviation = abbreviation if abbreviation==None else self.abbreviation
        self.name = name if name==None else self.name
        self.address = address if address==None else self.address

        if post:
            self(post('Update'))
    
    def getInfo(self):
        return {'Abbreviation': self.abbreviation,
                'Name': self.name,
                'Address': self.address}

    def post(self, action='InsertOrUpdate'):
        #Valid actions 'Insert', 'Update', 'InsertOrUpdate', 'InsertOrUpdateNonEmptyFields'
        
        data = {
            "APIKEY": APIKEY,
            "mvInventoryLocation ": {
                "InventoryLocationAbbreviation": self.abbreviation,
                "InventoryLocationName": self.name,
                "InventoryLocationAddress": self.address,
            },
            "mvRecordAction": action
            }
        return requests.post('https://api.megaventory.com/v2017a/Product/ProductUpdate', json=data)