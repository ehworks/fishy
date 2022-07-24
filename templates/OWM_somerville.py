import sys

import requests
import datetime
import os
from tkinter import *
from tkinter import Tk, Text
from tkinter import messagebox


# root = Tk()
# window = Tk()
# window.title("weather today")
# window.config(padx=20, pady=20)


#
# canvas = Canvas(height=400, width=400)
#
# fish_img = PhotoImage(file="C:/Users/m_els/PycharmProjects/pythonProject1/Fishy/static/blackFish.png")
#
# canvas.create_image(200, 200, image=fish_img)
# canvas.grid(row=0, column=1)

# canvas.create_text(300, 300, text='helloe')
# canvas.pack()
#
# weather_code = Label(text="hourly weather :")
# weather_code.grid(row=2, column=1)


# window.mainloop()

# weather data begins
# api.openweathermap.org
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

api_key = "8b51b39e9f385d1891a47974321b2a43"
account_sid = 'ACaaa4f45f3fe7cebac1a493df335e2ab4'
auth_token = "c548b62c1c60ec4ae37301f601cdbdc7"


# location for open weather somerville TX
# MY_LAT = 30.347830
# MY_LONG = -96.613351

# lake somerville
MY_LAT = 30.306192
MY_LONG = -96.618576
print("Lake Somerville")



# new bern
# MY_LAT = 35.108494
# MY_LONG = -77.044113
# print("New Bern")

weather_param = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_param)

response.raise_for_status()
print(response)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False


with open('data.txt', "w") as data_file:
    # data_file.write()
    if MY_LONG == -77.044113:
        print("New Bern NC", file=data_file)
        print("/", file=data_file)
    else:
        print("Somerville TX", file=data_file)
        print("/", file=data_file)

    for hour_data in weather_slice:
        condition_code = hour_data["weather"][0]["id"]
        time_code = hour_data["dt"]

        # print(condition_code)

        epochtime = time_code
        time = datetime.datetime.fromtimestamp(epochtime)
        # print(time, file=data_file)


        if int(condition_code) < 700:
            will_rain = True
            print(condition_code)
            print(time, file=data_file)
            print(time)
            print("Possible Rain\n", file=data_file)
            print("/", file=data_file)
            print("Possible Rain\n")
            # epochtime = time_code
            # time = datetime.datetime.fromtimestamp(epochtime)
            # print(time, file=data_file)

            print()

        if int(condition_code) < 300:
            print(condition_code)
            print(time, file=data_file)
            print(time)
            print("possible ThunderStorm\n", file=data_file)
            print("/", file=data_file)
            print("possible ThunderStorm\n")

            epochtime = time_code
            time = datetime.datetime.fromtimestamp(epochtime)

            # print(time)

            print(condition_code)
            print()

        else:
            # for code in condition_code:
            # if condition_code > 800:
            # print(condition_code)
            #     print("Gonna Be good", file=data_file)

            if condition_code == 800:
                print(condition_code)
                # print(time, file=data_file)
                print(time)
                print("Nice Day, Clear Skies\n")
                print()

            if condition_code == 801:
                print(condition_code)
                # print(time, file=data_file)
                print(time)
                print("Nice Day, Few Clouds\n")
                print()

            if condition_code == 802:
                print(condition_code)
                # print(time, file=data_file)
                # print("Nice Day, Scattered Clouds\n", file=data_file)
                print(time)
                print("Nice Day, Scattered Clouds\n")

                print()

            if condition_code > 802:
                print(condition_code)
                print(time, file=data_file)
                print(time)
                print("Over Cast\n", file=data_file)
                print("/", file=data_file)
                print("Over Cast\n")
                print()
                epochtime = time_code
                time = datetime.datetime.fromtimestamp(epochtime)

                # print(time, file=data_file)
                print()

# data_file.write()
# window.mainloop()
