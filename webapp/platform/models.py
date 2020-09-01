class CarAttributes:
    def __init__(self, manufacturer_id, model_id, fuel, transmission, vin, mile_age, year, type, color):
        self.manufacturer = manufacturer_id
        self.model = model_id
        self.fuel = fuel
        self.transmission = transmission
        self.vin = vin
        self.mileage = mile_age
        self.year = year
        self.type = type
        self.color = color

class CarListing:
    def __init__(self, id, date, author_id, author_phone, state, car_attributes, price_true, price_predicted):
        self.id = id
        self.date = date
        self.author_id = author_id
        self.author_phone = author_phone
        self.state = state
        self.car_attributes = car_attributes
        self.price_true = price_true
        self.price_predicted = price_predicted
