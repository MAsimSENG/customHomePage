from flask import Flask,request,redirect
from flask import render_template
import getPrayerTimes
import mysql.connector as mysql



app = Flask(__name__)

myList=[]

def addToDB(value):
    cursor = db.cursor()
    query = "INSERT INTO list(item) VALUES (%s)"
    cursor.execute(query, (value,))
    db.commit()

def removeFromDB(value):
    cursor = db.cursor()
    query = "DELETE FROM list WHERE item = %s";
    cursor.execute(query, (value,))
    db.commit()



def getFromDB():
    query = "SELECT * FROM list"
    cursor.execute(query)
    values = cursor.fetchall()
    return values


@app.route('/')
def test():
    prayer_list = getPrayerTimes.getPrayerTimes("http://org.thebcma.com/victoria")
    temp = getPrayerTimes.getWeather("https://weather.gc.ca/city/pages/bc-66_metric_e.html")
    l = getFromDB()
    return render_template('index.html',rows=prayer_list,temp=temp, list=l)


@app.route('/todo', methods=['POST'])
def todo():
    addToDB(request.form['addthis'])

    return redirect('/')


@app.route('/del', methods=['POST'])
def del_item():
    line = request.get_data().decode(('utf-8'))
    removeFromDB(line)
    return redirect('/')


if __name__ == "__main__":
    db = mysql.connect(
        host = "localhost",
        user = "root",
        passwd = "MyNewPass",
        database = "todolist"
    )
    cursor = db.cursor()
    app.run(debug=False, host='localhost', port=8080)
