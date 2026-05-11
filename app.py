from flask import Flask, request
import mysql.connector   
app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="studentdb"
)
cursor = db.cursor()

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    cursor.execute("INSERT INTO students (name) VALUES (%s)", (name,))
    db.commit()
    return "Data Stored Successfully"

app.run(debug=True)  