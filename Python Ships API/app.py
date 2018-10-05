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
    query = "SELECT name FROM ships"
    ships = cursor.execute(query)
    return jsonify(str(ships))
