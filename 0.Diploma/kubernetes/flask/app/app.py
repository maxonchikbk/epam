from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
import requests
from waitress import serve
from prometheus_flask_exporter import PrometheusMetrics
import psycopg2
from flask_cors import CORS
import os 

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get("POSTGRES_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False # Sensitive
# CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
metrics = PrometheusMetrics(app)

con = psycopg2.connect(
    database=os.environ.get("POSTGRES_DB"),
    user=os.environ.get("POSTGRES_USER"),
    password=os.environ.get("POSTGRES_PASSWORD"),
    host="postgres"
    )
    
cur = con.cursor()

class Covid(db.Model):
    __tablename__ = 'covid'
    
    id = db.Column(db.Integer, primary_key=True)
    country_code= db.Column(db.String())
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

@app.route('/json')
def jsonfunc():
    cur.execute('DELETE FROM covid')
    uri = "https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/2021-01-01/2021-12-31"
    uresponse = requests.get(uri)
    jresponse = uresponse.text
    jsonf = json.loads(jresponse)
    for dv in jsonf['data']:                
        for cc in jsonf['data'][dv]:                    
            data = jsonf['data'][dv][cc]                    
            new_entry = Covid(country_code=data['country_code'], date_value=data['date_value'], confirmed=data['confirmed'], deaths=data['deaths'], stringency_actual=data['stringency_actual'], stringency=data['stringency'])
            db.session.add(new_entry)
            db.session.commit()
    return "Done!"

@app.route('/getall')
def getall():
    cur.execute('SELECT * FROM covid')
    rows = cur.fetchall()
    response = jsonify(rows)    
    return response

@app.route('/get/')
def getdate():
    entry_id = request.args.get('entry_id')
    print(entry_id)
    cur.execute("SELECT * from covid where country_code = '%s' order by date_value" % id)
    rows = cur.fetchall()
    response = jsonify(rows)    
    return response  

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)