from typing import List, Dict
from flask import Flask
import mysql.connector
import json
from flask import request, render_template, session, redirect, url_for
import pandas as pd


app = Flask(__name__)

df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c--', 'd', 'e']})

def people_data():
    config = { 'user': 'root', 'password': 'root', 'host': 'db', 'port': '3306', 'database': 'census' }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM people_data')
    
    dfObj = pd.DataFrame(columns=["Name", "Gender", "Age"])
    for (name, gender, age) in cursor:
        dfObj = dfObj.append({'Name' : name , 'Gender' : gender, 'Age' : age} , ignore_index=True)

    cursor.close()
    connection.close()

    return dfObj

def inject_data(name, gender, age):
    config = { 'user': 'root', 'password': 'root', 'host': 'db', 'port': '3306', 'database': 'census' }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO people_data VALUES ("{name}", "{gender}", {age})'.format(name=name, gender=gender, age=int(age)))

    connection.commit()
    cursor.close()
    connection.close()

    return 

@app.route('/', methods=["GET"])
def html_table():

    dfObj = people_data()

    return render_template('simple.html',  tables=[dfObj.to_html(classes="data")], titles=dfObj.columns.values)

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    name, gender, age = processed_text.split(",")

    inject_data(name, gender, age)

    return redirect(url_for('html_table'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
