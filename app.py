from flask import Flask , render_template, request, json
from connectdb import connection
import gviz_api
import json
import requests


app = Flask(__name__)

# This API receives data from the various sensors and stores the
# data in the database
@app.route('/connected', methods = ['POST'])
def insertIntoDB():
    url = 'http://127.0.0.1:5000'
    # Check to see if the request type is right
    if request.method == 'POST':
        data = request.get_json()
        room = data.get("LectureRoom")
        occupancy = data.get("Occupancy")
        airQuality = data.get("AirQualityLevel")
        try:
            c, conn = connection()
            # Update the database
            sql = "UPDATE ROOMINFORMATION SET Occupancy = %s , AirQualityLevel = %s WHERE LectureRoom = %s"
            value =(occupancy, airQuality, room)
            c.execute(sql,value)
            conn.commit()
            response = requests.post(url, data=data)
            return 'Request successful', 200
        except Exception as e:
            return (str(e))

        finally:
            #closing database connection.
            if(conn.is_connected()):
                conn.close()
                c.close()
                print("connection is closed")





#This API makes a connection to the database and retrieves information about the lecture
# It sends this information to the html page where the charts are rendered 
@app.route("/",methods = ['GET'])
def getDataFromDb():
    # Check to see if the request type is right
    if request.method == "GET":
        final = []
        try:
            c, conn = connection()
            sql = "SELECT * from RoomInformation"
            c.execute(sql)
            results = c.fetchall()
            for result in results:
                data = [
                        result[0],result[1],float(result[2])
                ]
                final.append(data)
        except Exception as e:
            return (str(e))

        finally:
            #closing database connection.
            if(conn.is_connected()):
                conn.close()
                c.close()
                print("connection is closed")

        return render_template('charts.html', rows=final)


if __name__ == '__main__':
    app.run()