from flask import Flask , render_template, request, json
from connectdb import connection
import gviz_api
import json


app = Flask(__name__)


@app.route('/connected', methods = ['POST'])
def insertIntoDB():
    if request.method == 'POST':
        data = request.get_json()
        room = data.get("LectureRoom")
        occupancy = data.get("Occupancy")
        airQuality = data.get("AirQualityLevel")
        try:
            c, conn = connection()
            sql = "INSERT INTO RoomInformation (LectureRoom, Occupancy, AirQualityLevel) VALUES (%s, %s, %s)"
            value =(room, occupancy, airQuality)
            c.execute(sql, value)
            conn.commit()
            return 'Worked', 200
        except Exception as e:
            return (str(e))





#This API makes a connection to the database and retrieves information about the lecture 
@app.route("/")
def getDataFromDb()():
    final = []
    c, conn = connection()
    sql = "SELECT * from RoomInformation"
    c.execute(sql)
    results = c.fetchall()
    for result in results:
        data = [
                result[0],result[1],result[2]
        ] 
        final.append(data)
    return render_template('charts.html', rows=final)

if __name__ == '__main__':
    app.run(debug=True)