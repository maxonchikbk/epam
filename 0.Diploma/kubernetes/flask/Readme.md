virtualenv env
source env/bin/activate
pip install 
python -m pip freeze > requirements.txt
export DATABASE_URL="postgresql://user:password@192.168.1.38:30008/database"

psql -h 192.168.1.43 -p 30008 -U user database

CREATE TABLE covid (
    id INT PRIMARY KEY,
    country_code TEXT NOT NULL,
    date_value TEXT NOT NULL,
    confirmed INT NOT NULL,
    deaths INT NOT NULL,
    stringency_actual TEXT NOT NULL,
    stringency TEXT NOT NULL
);


country_code= db.Column(db.String())
    date_value = db.Column(db.String())
    confirmed = db.Column(db.Integer())
    deaths = db.Column(db.Integer())
    stringency_actual = db.Column(db.String())
    stringency = db.Column(db.String())