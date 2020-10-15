import unittest
import datetime
from ..webapp_platform.models import CarListing, CarListingSchema, CarAttributes

class TestValFunction(unittest.TestCase):
    expected_value = CarListing("1234", datetime.date(2019, 10, 1), "001", "0542271836", "USA",
                                CarAttributes("345", "A8790", "gas", "automatic", "1FTFW1EF8EFA71429",
                                              4000, 1990, "sedan", "gray"), 900)

    def create_value(self, id = "1234", date = "2019-10-1", author_id = "001", author_phone = "0542271836", state = "USA",
                     manufacturer_id = "345", model_id = "A8790", fuel = "gas", transmission = "automatic",
                     vin = "1FTFW1EF8EFA71429", mileage =  4000, year = 1990, type = "sedan", color = "gray",
                     customer_price = 900):
        list_keys = ['id', 'date', 'author_id', 'author_phone', 'state', 'car_attributes', 'customer_price']
        car_attributes_keys = ["manufacturer_id", "model_id", "fuel", "transmission", "vin", "mileage", "year", "type", "color"]
        car_attributes_values = [manufacturer_id, model_id, fuel, transmission, vin, mileage, year, type, color]
        car_attributes_dict = dict(zip(car_attributes_keys, car_attributes_values))
        list_values = [id, date, author_id, author_phone, state, car_attributes_dict, customer_price]
        dict1 = dict(zip(list_keys, list_values))
        return dict1

    def test_val_function_ok(self):
        value = self.create_value()
        actual_value = CarListingSchema().load(value)
        self.assertTrue(isinstance(actual_value, CarListing))
        self.assertTrue(self.expected_value == actual_value)

    def test_val_date(self):
        value = self.create_value(date ="2019/10/1")
        actual_value = CarListingSchema().load(value)
        self.assertTrue(isinstance(actual_value, CarListing))
        self.assertTrue(self.expected_value == actual_value)

    def test_val_author_id(self):
        value = self.create_value(author_id = 1)
        actual_value = CarListingSchema().load(value)
        self.assertTrue(isinstance(actual_value, CarListing))
        self.assertTrue(self.expected_value == actual_value)

    def test_val_manufacturer_id(self):
        value = self.create_value(manufacturer_id = 111)
        actual_value = CarListingSchema().load(value)
        self.assertTrue(isinstance(actual_value, CarListing))
        self.assertTrue(self.expected_value == actual_value)

    def test_val_year(self):
        value = self.create_value(year = 2029)
        actual_value = CarListingSchema().load(value)
        self.assertTrue(isinstance(actual_value, CarListing))
        self.assertTrue(self.expected_value == actual_value)

    def test_val_fuel(self):
        value = self.create_value(fuel = 'not_gas')
        actual_value = CarListingSchema().load(value)
        self.assertTrue(isinstance(actual_value, CarListing))
        self.assertTrue(self.expected_value == actual_value)

    def test_val_type(self):
        value = self.create_value(type = 'sport')
        actual_value = CarListingSchema().load(value)
        self.assertTrue(isinstance(actual_value, CarListing))
        self.assertTrue(self.expected_value == actual_value)

if __name__ == '__main__':
    unittest.main()
