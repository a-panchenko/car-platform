import datetime

def date_validation(value):
    year = value.year
    if year < 1950 or year > datetime.datetime.now().year:
        raise ValueError("Invalide year")