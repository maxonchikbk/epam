from app import db

class Covid(db.Model):
    __tablename__ = 'covid'

    id = db.Column(db.String(), primary_key=True)
    country_code = db.Column(db.String())
    date_value = db.Column(db.String())
    confirmed = db.Column(db.String())
    deaths = db.Column(db.String())
    stringency_actual = db.Column(db.String())
    stringency = db.Column(db.String())

    def __init__(self, date_value, confirmed, deaths, stringency_actual, stringency):
        self.country_code = country_code
        self.date_value = date_value
        self.confirmed = confirmed
        self.deaths = deaths
        self.stringency_actual = stringency_actual
        self.stringency = stringency

    def __repr__(self):
        return f"<Country {self.country_code}>"