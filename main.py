from Product import Product
from SupplierClient import SupplierClient
from InventoryLocation import InventoryLocation
from Tax import Tax
from Discount import Discount
from SalesOrder import SalesOrder
# Create Objects
shoes = Product('1112256', 'Nike shoes', 99.99, 44.99)
babis = SupplierClient('Babis', 'babis@exampletest.com ', 'Example 8, Athens', '1235698967')
warehouse = InventoryLocation('Main', 'Main Location', 'Example 20, Athens')
tax = Tax('Taxation', 0.24)
loyaltyDiscount = Discount('Loyalty Discount', 0.5)
# Post them in the database
clientResponce = babis.post().json()
productResponce = shoes.post().json()
warehouseResponce = warehouse.post().json()
taxResponce = tax.post().json()
discountResponce = loyaltyDiscount.post().json()
# Create and post the order
orderResponce = SalesOrder(productResponce['mvProduct']['ProductSKU'],
                            2,
                            productResponce['mvProduct']['ProductSellingPrice'],
                            clientResponce['mvSupplierClient']['SupplierClientID'],
                            warehouseResponce['mvInventoryLocation']['InventoryLocationID'],
                            taxResponce['mvTax']['TaxValue'],
                            discountResponce['mvDiscount']['DiscountValue'], 'Verified').post('Verified').json()