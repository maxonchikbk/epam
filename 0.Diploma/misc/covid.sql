CREATE TABLE covid(
    
    date_value VARCHAR,     
    country_code VARCHAR NOT NULL PRIMARY KEY,
    confirmed INT NOT NULL,
    deaths INT NOT NULL,
    stringency_actual VARCHAR,
    stringency VARCHAR
);

WITH covid_json (doc) AS (VALUES(
'[
    {
        "date_value": "2021-01-01",
        "country_code": "AFG",
        "confirmed": 52513,
        "deaths": 2201,
        "stringency_actual": 12.04,
        "stringency": 12.04
    },
    {        
        "date_value": "2021-01-01",
        "country_code": "ALB",
        "confirmed": 58316,
        "deaths": 1181,
        "stringency_actual": 56.48,
        "stringency": 56.48
    },
    {
        "date_value": "2021-01-01",
        "country_code": "DZA",
        "confirmed": 99897,
        "deaths": 2762,
        "stringency_actual": 72.22,
        "stringency": 72.22
    },
    {
        "date_value": "2021-01-01",
        "country_code": "AND",
        "confirmed": 8117,
        "deaths": 84,
        "stringency_actual": 52.78,
        "stringency": 52.78
    },
    {
        "date_value": "2021-01-01",
        "country_code": "AGO",
        "confirmed": 17568,
        "deaths": 405,
        "stringency_actual": 65.74,
        "stringency": 65.74
    }
]'::json))
INSERT INTO covid (id, date_value, country_code, confirmed, deaths,stringency_actual,stringency)
SELECT p.* FROM covid_json l CROSS JOIN lateral
json_populate_recordset(NULL::covid, doc) AS p;