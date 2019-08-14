from flask import Flask
from flask import render_template
import getPrayerTimes

app = Flask(__name__)


@app.route('/')
def test():
    prayer_list = getPrayerTimes.getPrayerTimes("http://org.thebcma.com/victoria")
    temp = getPrayerTimes.getWeather("https://weather.gc.ca/city/pages/bc-66_metric_e.html")

    return render_template('index.html',rows=prayer_list,temp=temp)


if __name__ == "__main__":
    app.run(debug=False, host='localhost', port=8080)
