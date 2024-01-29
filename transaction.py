import random
from datetime import datetime
from enum import Enum
from faker import Faker
from faker.providers import company, geo, phone_number, ssn, sbn

fake = Faker()
fake.add_provider(geo)
fake.add_provider(company)
fake.add_provider(phone_number)
fake.add_provider(ssn)
fake.add_provider(sbn)


class SupplyChain(Enum):
    HARVESTING = "harvesting"
    COOLING = "cooling"
    PACKING = "packing"
    SHIPPING = "shipping"
    RECEIVING = "receiving"


class Commodity(Enum):
    CHEESE = 1
    SHELL_EGGS = 2
    NUT_BUTTER = 3
    CUCUMBER = 4
    HERBS = 5
    LEAFY_GREENS = 6
    MELONS = 7
    PEPPERS = 8
    SPROUTS = 9
    TOMATOES = 10
    TROPICAL_TREE_FRUITS = 11
    FRUITS = 12
    FINFISH = 13
    DELI_SALADS = 14

# ! This is done to deal with JSONDecodeError due to inconsistency in quotes.
def get_GPS_coords():
    coords_on_land = fake.location_on_land(coords_only=True)
    coords_on_land = f'{(float(coords_on_land[0]), float(coords_on_land[1]))}'
    return coords_on_land

transactions = {
    "harvesting": {
        "type": "harvesting",
        "timestamp": str(datetime.now().timestamp()),
        "bname": fake.company(),
        "bphone": fake.msisdn(),
        "commodity": random.choice(list(Commodity)).name,
        "variety": "Regular",
        "location": get_GPS_coords(),  # field_location
        "measurement": f"{random.randint(1, 19)} boxes",
        "license_no": fake.ssn(),
        "message": "",
        "flagged": "N",
    },
    "cooling": {
        "type": "cooling",
        "timestamp": datetime.now().timestamp(),  # ALTERNATE : date_of_cooling
        "bname": fake.company(),
        "bphone": fake.msisdn(),
        "commodity": random.choice(list(Commodity)).name,
        "variety": "Regular",
        "location": get_GPS_coords(),  # ALTERNATE: cooling_location
        "license_no": fake.ssn(),
        "message": "",
        "flagged": "N",
    },
    "packing": {
        "type": "packing",
        "timestamp": datetime.now().timestamp(),  # ALTERNATE: date_of_packing
        "bname": fake.company(),
        "bphone": fake.msisdn(),
        "commodity": random.choice(list(Commodity)).name,
        "variety": "Regular",
        "location": get_GPS_coords(),  # ALTERNATE: packing_location
        "lot_code": fake.sbn9(),
        "license_no": fake.ssn(),
        "message": "",
        "flagged": "N",
    },
    "shipping": {
        "type": "shipping",
        "timestamp": datetime.now().timestamp(),  # ALTERNATE: date_of_shipping
        "bname": fake.company(),
        "bphone": fake.msisdn(),
        "commodity": random.choice(list(Commodity)).name,
        "variety": "Regular",
        "init_loc": get_GPS_coords(),
        "dest_loc": get_GPS_coords(),
        "license_no": fake.ssn(),
        "message": "",
        "flagged": "N",
    },
    "receiving": {
        "type": "receiving",
        "timestamp": datetime.now().timestamp(),  # ALTERNATE: date_of_receiving
        "bname": fake.company(),
        "bphone": fake.msisdn(),
        "commodity": random.choice(list(Commodity)).name,
        "variety": "Regular",
        "location": get_GPS_coords(),  # ALTERNATE : receiving_location
        "license_no": fake.ssn(),
        "message": "",
        "flagged": "N",
    },
}

def create_transaction(user_type: SupplyChain, flagged: bool, message: str, commodity: Commodity) -> dict:
    transaction_template = transactions[user_type.value]
    transaction_template["flagged"] = "Y" if flagged else "N"
    transaction_template["message"] = message
    transaction_template["commodity"] = commodity.name
    print(transaction_template)
    return transaction_template

if __name__=="__main__":
    # * Prints all the templates present
    print(transactions["harvesting"])
    print(transactions["cooling"])
    print(transactions["packing"])
    print(transactions["shipping"])
    print(transactions["receiving"])