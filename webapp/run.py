from flask import Flask
from flask import request
from flask_api import status
from webapp_platform.models import CarListingSchema, CarListing
from webapp_platform.services import PricePredictor
import inflection
from marshmallow import ValidationError
from pprint import pprint

app = Flask(__name__)

__predictor = PricePredictor()

@app.route('/ping')
def pong():
    return 'pong'

@app.route('/car-listings', methods=['POST'])
def upload_car_listing():
    # get JSON data from the output
    req_data = request.get_json()

    # converting key camel case to snack case with inflection library
    req_data = {inflection.underscore(i): j for i, j in req_data.items()}
    req_data['car_attributes'] = {inflection.underscore(i): j for i, j in req_data['car_attributes'].items()}

    # input validation
    try:
        #load function returns dictionary
        car_listing = CarListingSchema().load(req_data)
        print(car_listing.__dict__)
        prediction = __predictor.predict(car_listing)
        return prediction, status.HTTP_200_OK
    except ValidationError as err:
        pprint(err.messages)
        return err.messages, status.HTTP_400_BAD_REQUEST

if __name__ == '__main__':
    app.run(debug=True)
