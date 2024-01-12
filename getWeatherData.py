import re
import requests
from bs4 import BeautifulSoup
from os.path import exists
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


# dialog-box for first time use only
class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Weather-coverage")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.entry_city = Gtk.Entry()
        self.entry_city.set_text("Enter city")
        self.box.pack_start(self.entry_city, True, True, 0)

        self.entry_zip_code = Gtk.Entry()
        self.entry_zip_code.set_text("Enter zip-code")
        self.box.pack_start(self.entry_zip_code, True, True, 0)

        self.button1 = Gtk.Button(label="done")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

    def on_button1_clicked(self, widget):
        city = self.entry_city.get_text()
        zip_code = self.entry_zip_code.get_text()

        file = open("location-data.txt", "w")
        file.write(city + "\n")
        file.write(zip_code + "\n")
        Gtk.main_quit()


# pop-up window for city and zip-code data if text-file does not exist
if not exists("location-data.txt"):
    win = MyWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

with open("location-data.txt", "r") as f:
    data = f.read()

city, zipcode = data.split()


# scrape weather data
def ScrapeWeather(
    target_url="https://www.accuweather.com/en/us/"
    + city
    + "/"
    + zipcode
    + "/current-weather/337544",
):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }

    resp = requests.get(target_url, headers=headers).text
    soup = BeautifulSoup(resp, "html.parser")

    currentWeather = soup.find_all("div", {"class": "current-weather-details"})

    return currentWeather

weatherInfo = str(ScrapeWeather()).split('class')
cleanedInfo = []
replaceTxt = ['"detail-item spaced-content"', '<div>', '</div>', '\n', '<div', '=']
for line in range(len(weatherInfo)):
    info = weatherInfo[line]
    for txt in replaceTxt:
        info = info.replace(txt, '')
    cleanedInfo.append(info)
    