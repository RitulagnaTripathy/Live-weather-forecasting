import os
from bs4 import BeautifulSoup
import requests
from gtts import gTTS
from playsound import playsound

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    city=city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()

    weather_forecast=location+'\n'+time+'\n'+info+'\n'+weather+"°C"+'\n'
    print(weather_forecast)
    speech = gTTS(text=weather_forecast, lang='en', slow=False)
    speech.save('weather.mp3')
    playsound('weather.mp3')

city=input("Enter the Name of Any City >>  ")
city=city+" weather"
print("Searching......\n")
weather(city)
