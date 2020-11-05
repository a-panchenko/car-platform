import unittest
import datetime

from marshmallow.exceptions import ValidationError
from webapp_platform.models import CarListing, CarListingSchema, CarAttributes

class TestValidationFunction(unittest.TestCase):
    expected_value = CarListing("1234", datetime.date(2019, 10, 1), "001", "0542271836", "mn",
                                CarAttributes("345", "f-150", "gas", "automatic", "1FTFW1EF8EFA71429",
                                              4000, 1990, "sedan", "gray"), 900)

    def create_value(self, id = "1234", date = "2019-10-1", author_id = "001", author_phone = "0542271836", state = "mn",
                     manufacturer_id = "345", model_id = "f-150", fuel = "gas", transmission = "automatic",
                     vin = "1FTFW1EF8EFA71429", mileage =  4000, year = 1990, type = "sedan", color = "gray",
                     customer_price = 900):
        list_keys = ['id', 'date', 'author_id', 'author_phone', 'state', 'car_attributes', 'customer_price']
        car_attributes_keys = ["manufacturer_id", "model_id", "fuel", "transmission", "vin", "mileage", "year", "type", "color"]
        car_attributes_values = [manufacturer_id, model_id, fuel, transmission, vin, mileage, year, type, color]
        car_attributes_dict = dict(zip(car_attributes_keys, car_attributes_values))
        list_values = [id, date, author_id, author_phone, state, car_attributes_dict, customer_price]
        return dict(zip(list_keys, list_values))

    def test_validation_function_with_valid_data(self):
        value = self.create_value()
        actual_value = CarListingSchema().load(value)
        self.assertTrue(isinstance(actual_value, CarListing))
        self.assertTrue(self.expected_value == actual_value)

    def test_validation_invalid_format_date(self):
        value = self.create_value(date ="2019/10/1")
        with self.assertRaises(ValidationError):
            CarListingSchema().load(value)

    def test_validation_invalid_format_day(self):
        value = self.create_value(date ="2019-10-33")
        with self.assertRaises(ValidationError):
            CarListingSchema().load(value)

    def test_validation_date_invalid_year(self):
        value = self.create_value(date ="2029-10-1")
        with self.assertRaises(ValueError):
            CarListingSchema().load(value)

    def test_validation_invalid_author_id(self):
        value = self.create_value(author_id = 1)
        with self.assertRaises(ValidationError):
            CarListingSchema().load(value)

    def test_validation_invalid_manufacturer_id(self):
        value = self.create_value(manufacturer_id = 111)
        with self.assertRaises(ValidationError):
            CarListingSchema().load(value)

    def test_validation_invalid_year(self):
        value = self.create_value(year = 2029)
        with self.assertRaises(ValidationError):
            CarListingSchema().load(value)

    def test_validation_invalid_fuel(self):
        value = self.create_value(fuel = 'not_gas')
        with self.assertRaises(ValidationError):
            CarListingSchema().load(value)

    def test_validation_invalid_type(self):
        value = self.create_value(type = 'sport')
        with self.assertRaises(ValidationError):
            CarListingSchema().load(value)

if __name__ == '__main__':
    unittest.main()
