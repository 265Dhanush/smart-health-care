from flask import Flask, render_template , request
import mysql.connector
from database import mydb


app = Flask(__name__)


@app.route('/')
def hello_world():
  return render_template('home.html')


@app.route("/submit", methods=["POST"])
def submit_form():
    name = request.form["name"]
    age = request.form["age"]
    room_temperature = request.form["room_temperature"]
    room_humidity = request.form["room_humidity"]
    heart_rate = request.form["heart_rate"]
    body_temperature = request.form["body_temperature"]

    cursor = mydb.cursor()
    sql = "INSERT INTO patients (p_name,p_age,r_temp,r_humi,heart_rate,b_temp) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name, age, room_temperature, room_humidity, heart_rate, body_temperature)
    cursor.execute(sql, val)
    mydb.commit()

    return "Form submitted successfully"






if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
