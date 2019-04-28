from flask import Flask , render_template, request, json
from connectdb import connection
import gviz_api


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('charts.html')

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
            

            myresult = c.fetchall()
            for x in myresult:
                return str(x)
            
            
            
            
        except Exception as e:
            return (str(e))

@app.route('/getData')
def getFromDB():
    try:
        final = []
        c, conn = connection()
        sql = "SELECT * from RoomInformation"
        c.execute(sql)
        results = c.fetchall()
        for result in results:
           data = {
               "LectureRoom" : result[0],
               "Occupancy" : result[1],
               "AirQualityLevel" : result[2]
           } 
           final.append(data)

        description = {
            "LectureRoom" : ("string", "LectureRoom"),
            "Occupancy" : ("number", "Occupancy"),
            "AirQualityLevel" : ("number", "AirQualityLevel")
        }
        data_table = gviz_api.DataTable(description)
        data_table.LoadData(final)
        json = data_table.ToJSon(columns_order=("Lecture Room","Occupancy","Air Quality Level"))

        return json

    except Exception as e:
        return (str(e))
   
        
   



if __name__ == '__main__':
    app.run(debug=True)