from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request
from flask import jsonify
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Covid
from carmodels import CarsModel


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/covid', methods=['POST', 'GET'])
def handle_covid():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_entry = Covid(country_code=data['country_code'], date_value=data['date_value'], confirmed=data['confirmed'], deaths=data['deaths'], stringency_actual=data['stringency_actual'], stringency=data['stringency'], )
            db.session.add(new_entry)
            db.session.commit()
            return {"message": f"Entry {new_covid.new_entry} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        entries = Covid.query.all()
        results = [
            {
                "country_code": entry.country_code,
                "date_value": entry.date_value,
                "confirmed": entry.confirmed,
                "deaths": entry.deaths,
                "stringency_actual": entry.stringency_actual,
                "stringency": entry.stringency
            } for entry in entries]

        return {"count": len(results), "entries": results}

@app.route('/cars', methods=['POST', 'GET'])
def handle_cars():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_car = CarsModel(name=data['name'], model=data['model'], doors=data['doors'])
            db.session.add(new_car)
            db.session.commit()
            return {"message": f"car {new_car.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        cars = CarsModel.query.all()
        results = [
            {
                "name": car.name,
                "model": car.model,
                "doors": car.doors
            } for car in cars]

        return {"count": len(results), "cars": results}

@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()

    language = None
    framework = None
    python_version = None
    example = None
    boolean_test = None

    if request_data:
        if 'language' in request_data:
            language = request_data['language']

        if 'framework' in request_data:
            framework = request_data['framework']

        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['python']

        if 'examples' in request_data:
            if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                example = request_data['examples'][0]

        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)        