virtualenv env
source env/bin/activate
pip install flask_sqlalchemy
pip install flask_migrate 
pip install psycopg2-binary
python -m pip freeze > requirements.txt
export DATABASE_URL="postgresql://testuser:testpassword@192.168.1.38:30008/testdatabase"

psql -h 192.168.1.38 -p 30008 -U testuser testdatabase