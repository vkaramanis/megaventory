from Product import Product
from SupplierClient import SupplierClient
from Tax import Tax
from Discount import Discount

shoes = Product('1112256', 'Nike shoes', 99.99, 44.99)
babis = SupplierClient('Babis', 'babis@exampletest.com ', 'Example 8, Athens', '1235698967')

tax = Tax('Taxation', 0.24)
loyaltyDiscount = Discount('Loyalty Discount', 0.5)

clientResponce = babis.post().text
productResponce = shoes.post().text
taxResponce = tax.post().text
discountResponce = loyaltyDiscount.post().text
