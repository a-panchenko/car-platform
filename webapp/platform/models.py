class CarAttributes:
    def __init__(self, manufacturer_id, model_id, fuel, transmission, vin, mileage, year, type, color):
        self.manufacturer = manufacturer_id
        self.model = model_id
        self.fuel = fuel
        self.transmission = transmission
        self.vin = vin
        self.mileage = mileage
        self.year = year
        self.type = type
        self.color = color

class CarListing:
    def __init__(self, id, date, author_id, author_phone, state, car_attributes, customer_price, price_predicted):
        self.id = id
        self.date = date
        self.author_id = author_id
        self.author_phone = author_phone
        self.state = state
        self.car_attributes = car_attributes
        self.customer_price = customer_price
        self.price_predicted = price_predicted
