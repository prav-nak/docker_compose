from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)

def people_data() -> List[Dict]:
    config = { 'user': 'root', 'password': 'root', 'host': 'db', 'port': '3306', 'database': 'census' }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM people_data')
    results = [{name: [gender, age]} for (name, gender, age) in cursor]
    cursor.close()
    connection.close()

    return results

@app.route('/')
def index() -> str:
    return json.dumps({'people_data': people_data()})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
