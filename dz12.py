import time
import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime

while True:
    now = datetime.now()
    cur_time = now.strftime("%H:%M:%S")
    print("Time:", cur_time)

    url = 'https://ua.sinoptik.ua/погода-полтава'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    temp = soup.find(class_='today-temp').text

    print('Temperature in Poltava:', temp)

    connection = sqlite3.connect('itstep.sl3')

    connection.execute('''CREATE TABLE IF NOT EXISTS temperature (id INTEGER PRIMARY KEY AUTOINCREMENT, temp INTEGER, time TEXT)''')

    connection.execute("INSERT INTO temperature (temp, time) VALUES (?, ?)", (temp, cur_time))
    connection.commit()
    connection.close()

    time.sleep(1800)