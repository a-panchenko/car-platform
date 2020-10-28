from google.cloud import storage
import pickle
import pandas as pd

class PricePredictor:
    def __load_model(self):
        storage_client = storage.Client()
        bucket = storage_client.get_bucket('car_platform_gcs_bucket')
        blob = bucket.blob('models/lassoreg.sav')
        # Download the file to a destination
        blob.download_to_filename('./lassoreg.sav')
        return pickle.load(open('./lassoreg.sav', 'rb'))

    def __init__(self):
        self.loaded_model = self.__load_model()

    def convert_car_listing(self, car_listing):
        car_attributes = car_listing.__dict__['car_attributes']
        df = pd.DataFrame.from_dict(car_attributes.__dict__, orient='index').T
        df = df[['year', 'mileage']]
        return df

    def predict(self, car_listing):
        # load the model from disk
        df = self.convert_car_listing(car_listing)
        prediction = self.loaded_model.predict(df)
        return str(round(prediction[0]))
