# dependencies -------->
from flask import Flask, jsonify, request
from sqlalchemy import text, create_engine
from sqlalchemy.orm import Session
import psycopg2

# program variables -------->
app = Flask(__name__)

# db credentials -------->
user = 'admin'
passwd = 'admin'
port = 5432
db = 'exam'
uri = 'db'
engine = create_engine(f"postgresql://{user}:{passwd}@{uri}:{port}/{db}")

# SQL commands -------->
init = 'CREATE TABLE IF NOT EXISTS packages (id SERIAL PRIMARY KEY, status VARCHAR(50));'
list = 'SELECT * FROM packages;'
get = 'SELECT * FROM packages WHERE id = '
drop = 'DROP TABLE packages;'
insert = "INSERT INTO packages (status) VALUES ('registrado')"

# methods -------->
# make sure the db tables are created
def db_init():
    with Session(engine) as session:
        session.execute(text(init))
        session.commit()

# jsonify one element returned by the db query
def serialize_element(raw_data):
    return jsonify([{'id':raw_data.id, 'status':raw_data.status}])

# jsonify collection returned by the db query
def serialize_data(raw_data):
    result = []
    for it in raw_data:
        result.append({'id':it.id, 'status':it.status})

    return jsonify(result)

# endpoints -------->
# for testing purposes
@app.route('/drop', methods=['GET'])
def drop_table():
    with Session(engine) as session:
        session.execute(text(drop))
        session.commit()
    return 'Successful', 202

@app.route('/packages', methods=['GET'])
def get_packages():
    with Session(engine) as session:
        return serialize_data(session.execute(text(list))), 202

@app.route('/package/<int:id>', methods=['GET'])
def get_package_status(id):
    with Session(engine) as session:
        return serialize_data(session.execute(text(get + f'{id};'))), 202

@app.route('/package', methods=['POST'])
def create_package():
    with Session(engine) as session:
        session.execute(text(insert))
        session.commit()
    return serialize_element(session.execute(text(list)).all()[-1]), 202

@app.route('/package', methods=['PUT'])
def update_package_status():
    id = request.json.get('id')
    status = request.json.get('status')
    with Session(engine) as session:
        # package exists
        if len(session.execute(text(get + f'{id};')).all()) == 1:
            session.execute(text(f"UPDATE packages SET status='{status}' WHERE id = {id};"))
            session.commit()
            return serialize_data(session.execute(text(get + f'{id};'))), 202
        else:
            return "Package does not exist", 404

# program execution -------->
# init db if first connection
db_init()
# run web app
if __name__ == '__main__':
    app.run(debug=True)
