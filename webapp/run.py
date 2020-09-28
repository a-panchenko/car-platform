from flask import Flask
from flask import request
from flask_api import status
import webapp_platform.models as models
import inflection

app = Flask(__name__)

@app.route('/ping')
def pong():
    return 'pong'

@app.route('/car-listings', methods=['POST'])
def car_listing():
    # get JSON data from the output
    req_data = request.get_json()

    try:
        # converting key camel case to snack case with inflection library
        req_data = {inflection.underscore(i): j for i, j in req_data.items()}
        req_data['car_attributes'] = {inflection.underscore(i): j for i, j in req_data['car_attributes'].items()}

        # converting JSON data to classes
        car_attributes = models.CarAttributes(*req_data['car_attributes'].values())
        car_listing = models.CarListing(req_data['id'], req_data['date'], req_data['author_id'], req_data['author_phone'],
                                        req_data['state'], car_attributes.__dict__, req_data['customer_price'], req_data['price_predicted'])

        print(car_listing.__dict__)
        return 'OK'

    except KeyError:
        return "Invalid JSON structure", status.HTTP_400_BAD_REQUEST

if __name__ == '__main__':
    app.run(debug=True)