from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
from waitress import serve
from prometheus_flask_exporter import PrometheusMetrics
import psycopg2

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
metrics = PrometheusMetrics(app)

con = psycopg2.connect(
    database="testdatabase",
    user="testuser",
    password="testpassword",
    host="postgres")

cur = con.cursor()

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

@app.route('/getall')
def main():
    cur.execute('SELECT * FROM covid')
    rows = cur.fetchall()
    response = jsonify(rows)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

# @app.route('/')
# def hello():
#     return "Hello World!"
# @app.route('/jsonfile')
# def jsonfilefunc():
#     f = open('2021.json')
#     jsonf = json.load(f)
#     f.close()
#     for dv in jsonf['data']:                
#         for cc in jsonf['data'][dv]:                    
#             data = jsonf['data'][dv][cc]                    
#             new_entry = Covid(country_code=data['country_code'], date_value=data['date_value'], confirmed=data['confirmed'], deaths=data['deaths'], stringency_actual=data['stringency_actual'], stringency=data['stringency'])
#             db.session.add(new_entry)
#             db.session.commit()
#     return "Done!"


# @app.route('/getcovid', methods=['POST', 'GET'])
# def handle_covid():

#     if request.method == 'POST':
#         if request.is_json:
#             json = request.get_json(force=False, silent=False, cache=True)
            
#             for dv in json['data']:                
#                 for cc in json['data'][dv]:                    
#                     data = json['data'][dv][cc]                    
#                     new_entry = Covid(country_code=data['country_code'], date_value=data['date_value'], confirmed=data['confirmed'], deaths=data['deaths'], stringency_actual=data['stringency_actual'], stringency=data['stringency'])
#                     db.session.add(new_entry)
#                     db.session.commit()
                
#             return {"message": "entry {} has been created successfully.".format(new_entry.country_code)}
#         else:
#             return {"error": "The request payload is not in JSON format"}
        
#     elif request.method == 'GET':
#         covid = Covid.query.all()
#         results = [
#             {
#                 "country_code": entry.country_code,
#                 "date_value": entry.date_value,
#                 "confirmed": entry.confirmed,
#                 "deaths": entry.deaths,
#                 "stringency_actual": entry.stringency_actual,
#                 "stringency": entry.stringency                
#             } for entry in covid]

#         return {"count": len(results), "covid": results}

@app.route('/getcovid/')
def handle_entry():
    id = request.args.get('entry_id')
    print(id)
    cur.execute("SELECT * from covid where country_code = '%s' order by date_value" % id)
    rows = cur.fetchall()
    return jsonify(rows)    

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)