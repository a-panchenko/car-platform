from enum import Enum
from marshmallow import Schema, fields, validate, post_load
from webapp_platform.validation_functions import date_validation
import datetime

class CarAttributes:
    def __init__(self, manufacturer_id, model_id, fuel, transmission, vin, mileage, year, type, color):
        self.manufacturer_id = manufacturer_id
        self.model_id = model_id
        self.fuel = fuel
        self.transmission = transmission
        self.vin = vin
        self.mileage = mileage
        self.year = year
        self.type = type
        self.color = color

    def __eq__(self, other):
        return isinstance(other, CarAttributes) and self.manufacturer_id == other.manufacturer_id and \
               self.model_id == other.model_id and \
               self.fuel == other.fuel and \
               self.transmission == other.transmission and \
               self.vin == other.vin and \
               self.mileage == other.mileage and \
               self.year == other.year and \
               self.type == other.type and \
               self.color == other.color

class CarListing:
    def __init__(self, id, date, author_id, author_phone, state, car_attributes, customer_price):
        self.id = id
        self.date = date
        self.author_id = author_id
        self.author_phone = author_phone
        self.state = state
        self.car_attributes = car_attributes
        self.customer_price = customer_price

    def __eq__(self, other):
        return isinstance(other, CarListing) and self.id == other.id and \
               self.date == other.date and \
               self.author_id == other.author_id and \
               self.author_phone == other.author_phone and \
               self.state == other.state and \
               self.car_attributes == other.car_attributes and \
               self.customer_price == other.customer_price

class Fuel(Enum):
    gas = 'gas'
    diesel = 'diesel'

class Transmission(Enum):
    automatic = 'automatic'
    manual = 'manual'
    other = 'other'

class Type(Enum):
    hatchback = 'hatchback'
    pickup = 'pickup'
    sedan = 'sedan'
    wagon = 'wagon'
    van = 'van'
    truck = 'truck'

class Color(Enum):
    black = 'black'
    blue = 'blue'
    brown = 'brown'
    gray = 'gray'
    green = 'green'
    orange = 'orange'
    purple = 'purple'
    red = 'red'
    silver = 'silver'
    white = 'white'
    yellow = 'yellow'

class State(Enum):
    mn = 'mn'
    va = 'va'
    wi = 'wi'
    ca = 'ca'
    fl = 'fl'
    tx = 'tx'
    wa = 'wa'
    ny = 'ny'

class CarAttributesSchema(Schema):
    manufacturer_id = fields.Str(required=True)
    model_id = fields.Str(required=True)
    fuel = fields.Str(required=True, validate=validate.OneOf([k.value for k in Fuel]))
    transmission = fields.Str(required=True, validate=validate.OneOf([k.value for k in Transmission]))
    vin = fields.Str(required=True, validate=validate.Length(min=11, max=17))
    mileage = fields.Int(required=True, validate=validate.Range(min=0))
    year = fields.Int(required=True, validate=validate.Range(min=1950, max=datetime.datetime.now().year))
    type = fields.Str(required=True, validate=validate.OneOf([k.value for k in Type]))
    color = fields.Str(required=True, validate=validate.OneOf([k.value for k in Color]))

class CarListingSchema(Schema):
    id = fields.Str(required=True)
    date = fields.Date(required=True, validate=date_validation)
    author_id = fields.Str(required=True)
    author_phone = fields.Str(required=True, validate=validate.Length(min=3))
    state = fields.Str(required=True, validate=validate.OneOf([k.value for k in State]))
    car_attributes = fields.Nested(CarAttributesSchema)
    customer_price = fields.Int(required=True)

    @post_load
    def post_load_carlisting(self, dict, many, **kwargs):
        attributes = dict['car_attributes']
        attributes_obj = CarAttributes(attributes['manufacturer_id'], attributes['model_id'],
                                       attributes['fuel'], attributes['transmission'],
                                       attributes['vin'], attributes['mileage'], attributes['year'], attributes['type'], attributes['color'])
        return CarListing(dict['id'], dict['date'], dict['author_id'], dict['author_phone'],
                          dict['state'], attributes_obj, dict['customer_price'])
