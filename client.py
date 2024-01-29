import requests
from transaction import SupplyChain, create_transaction, Commodity

url = "http://127.0.0.1:5000/"

r1 = requests.post(url+"mine_block", json=create_transaction(SupplyChain.HARVESTING, flagged=False, message="Product good", commodity=Commodity.MELONS))
# print(r1)
r2 = requests.post(url+"mine_block", json=create_transaction(SupplyChain.COOLING, flagged=False, message="Product good", commodity=Commodity.MELONS))
# print(r2)
r3 = requests.post(url+"mine_block", json=create_transaction(SupplyChain.PACKING, flagged=False, message="Product good", commodity=Commodity.MELONS))
# print(r3)
r4 = requests.post(url+"mine_block", json=create_transaction(SupplyChain.SHIPPING, flagged=False, message="Product good", commodity=Commodity.MELONS))
# print(r4)
r5 = requests.post(url+"mine_block", json=create_transaction(SupplyChain.RECEIVING, flagged=False, message="Product good", commodity=Commodity.MELONS))
# print(r5)

r = requests.get(url+"get_chain")
print(r.text)

r_dot = requests.get(url+"get_transaction_type")
print(r_dot.text)

# r_all = requests.get(url+"print_all")
# print(r_all.text)