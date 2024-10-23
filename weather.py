from flask import Flask, request, render_template
import requests

app = Flask(__name__)
  
@app.route('/', methods =["GET", "POST"])
def index(): 
    weatherData = ''
    error = 0
    cityName = ''
    temp_celsius = ''
    message = ''
    if request.method == "POST":  
        weatherApiKey = '2ba56868930ce82ca35aadb64bd40c95'
        cityName = request.form.get("cityName")  
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={weatherApiKey}", verify=False) 
        
        if r.status_code != 200:
            weatherData = r.json()
            message = weatherData.get('message', '')
            return f'Error getting weather details for {cityName}. Error message : {message}'
        
        if r.status_code == 200:
                       
            weatherData = r.json()
            temp_celsius = round((weatherData['main']['temp'] - 273.15), 2)
            
    return render_template('index.html', data = weatherData, temp_celsius = temp_celsius, cityName = cityName)
    
if __name__ == "__main__":
    app.run(debug=True ,port=8085,use_reloader=True)