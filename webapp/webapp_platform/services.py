from google.cloud import storage
import pickle

class PricePredictor:
    def load_model(self):
        storage_client = storage.Client()
        bucket = storage_client.get_bucket('car_platform_gcs_bucket')
        blob = bucket.blob('models/lassoreg.sav')
        # Download the file to a destination
        blob.download_to_filename()
        return pickle.load(open('./lassoreg.sav', 'rb'))

    def __init__(self):
        self.loaded_model = self.load_model()

    def predict(self, car_listing):
        # load the model from disk
        return self.loaded_model.predict(car_listing)
