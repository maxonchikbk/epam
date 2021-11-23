from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request
from flask import jsonify

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Covid(db.Model):
    __tablename__ = 'covid'
    
    country_code= db.Column(db.String(), primary_key=True)
    date_value = db.Column(db.String())
    confirmed = db.Column(db.Integer())
    deaths = db.Column(db.Integer())
    stringency_actual = db.Column(db.String())
    stringency = db.Column(db.String())

    def __init__(self, country_code, date_value, confirmed, deaths, stringency_actual, stringency):
        self.country_code= country_code
        self.date_value = date_value
        self.confirmed = confirmed
        self.deaths = deaths
        self.stringency_actual = stringency_actual
        self.stringency = stringency

    def __repr__(self):
        return f"<Country {self.country_code}>"

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/covid', methods=['POST', 'GET'])
def handle_covid():

    if request.method == 'POST':
        if request.is_json:
            data = request.get_json(force=False, silent=False, cache=True)
            new_entry = Covid(country_code=data['country_code'], date_value=data['date_value'], confirmed=data['confirmed'], deaths=data['deaths'], stringency_actual=data['stringency_actual'], stringency=data['stringency'])
            db.session.add(new_entry)
            db.session.commit()
            return {"message": "entry {} has been created successfully.".format(new_entry.country_code)}
        else:
            return {"error": "The request payload is not in JSON format"}
        
    elif request.method == 'GET':
        covid = Covid.query.all()
        results = [
            {
                "country_code": entry.country_code,
                "date_value": entry.date_value,
                "confirmed": entry.confirmed,
                "deaths": entry.deaths,
                "stringency_actual": entry.stringency_actual,
                "stringency": entry.stringency                
            } for entry in covid]

        return {"count": len(results), "covid": results}

@app.route('/covid/<entry_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_entry(entry_id):
    entry = Covid.query.get_or_404(entry_id)

    if request.method == 'GET':
        response = {
            "country_code": entry.country_code,
                "date_value": entry.date_value,
                "confirmed": entry.confirmed,
                "deaths": entry.deaths,
                "stringency_actual": entry.stringency_actual,
                "stringency": entry.stringency   
        }
        return {"message": "success", "entry": response}

    elif request.method == 'PUT':        
        data = request.get_json()
        country_code=data['country_code']
        date_value=data['date_value']
        confirmed=data['confirmed']
        deaths=data['deaths']
        stringency_actual=data['stringency_actual']
        stringency=data['stringency']        
        db.session.add(entry)
        db.session.commit()
        return {"message": f"Entry {entry.country_code} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(entry)
        db.session.commit()
        return {"message": f"Entry {entry.country_code} successfully deleted"}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')