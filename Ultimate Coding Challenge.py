import json
import requests 

#A module must be installed on python, which allows us to send requests to this API. Open command prompt and type 'pip install requests' or 'pall requests'

API_KEY = "41e63746f56bd08b38c4a62e59f29932"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(City, Country):
    #building a url that is similar to "BASE_URL" That includes the chosen City and API Key in order to send the request
    #passing the query parameter through the API key

    #separate url requests for both country and city 
    city_request_url = f"{BASE_URL}?appid={API_KEY}&q={City}&units=metric"
    country_request_url = f"{BASE_URL}?appid={API_KEY}&q={Country}&units=metric"

    #Next step is to send the HTTP request e.g. post put delete. in this instance i need a Get request because i'm retrieving information 
    #obtains get request from the request module that was downloaded through the import command. Response will contain the data needed.

    response = requests.get(city_request_url)

    #Need to check if response is successful. 200 means successful

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        #The location is the City because we had a valid City
        answer = '{ "params": [{ "name": "temperature", "value": ' + str(temperature) + ' }, {"name": "location", "value": "' + City + '"}]}'
        #Calling Json function to parse string into Json
        return json.loads(answer)

    else: 
        #Initial request was unsuccessful therefore, trying with Country. 
        response = requests.get(country_request_url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            #Location is set to Country because there was an ivalid City 
            answer = '{ "params": [{ "name": "temperature", "value": ' + str(temperature) + ' }, {"name": "location", "value": "' + Country + '"}] }'
            #Calling Json function to parse string into Json
            return json.loads(answer)
        else:
            #When an incorrect City is used the API falls back the Country
            answer = '{ "error":" An error occurred, invalid City and Country " }'
            #Calling Json function to parse string into Json
            return json.loads(answer)
        
#Query parameters need to be sent (specifying what data we want)
City = input("Enter a city name: ")
Country = input("Enter a country: ")
print(get_weather(City, Country))