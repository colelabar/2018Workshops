from flask import Flask, jsonify, request, json
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'apidb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

@app.route('/ships', methods=['GET'])
def allShips():
    query = cursor.execute("SELECT * FROM ships")
    return jsonify(cursor.fetchall())

@app.route('/ships/<int:ship_id>', methods=['GET'])
def oneShip(ship_id):
    id = ship_id
    query = cursor.execute("SELECT * FROM ships WHERE id=" + str(id))
    return jsonify(cursor.fetchone())

@app.route('/ships/<int:ship_id>', methods=['DELETE'])
def oneShip(ship_id):
    id = ship_id
    query = cursor.execute("DELETE * FROM ships WHERE id=" + str(id))
    # Playing with return conditionals
