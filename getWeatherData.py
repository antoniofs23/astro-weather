import re
import requests
from bs4 import BeautifulSoup
from os.path import exists
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

"""
Define pop-up window that will collect link to be scraped
"""


# dialog-box for first time use only
class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Weather-coverage")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.entry_link = Gtk.Entry()
        self.entry_link.set_text("enter link here for accuweather")
        self.box.pack_start(self.entry_link, True, True, 0)

        self.button1 = Gtk.Button(label="done")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

    def on_button1_clicked(self, widget):
        link = self.entry_link.get_text()

        file = open("location-data-link.txt", "w")
        file.write(link)
        Gtk.main_quit()


def pop_up_win():
    # pop-up window for city and zip-code data if text-file does not exist
    if not exists("location-data-link.txt"):
        win = MyWindow()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    with open("location-data-link.txt", "r") as f:
        link_text = f.read()

    return link_text


"""
Scrape personal accuweather link with your city/zip-code
"""


# scrape weather data
def ScrapeWeather(target_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }

    resp = requests.get(target_url, headers=headers).text
    soup = BeautifulSoup(resp, "html.parser")

    weatherInfo = soup.find_all("div", {"class": "current-weather-details"})

    # clean the scraped data using regular expressions
    # the "<.*?>" removes html tags
    patterns = ["<.*?>", "\n", "®", "°", "%", "™"]

    # to remove multiple patterns need to use the "|" or regex pipe
    cleanedInfo = re.sub("|".join(patterns), "", str(weatherInfo))

    # now we just want the numbers which we can get from regular expressions yet again
    mesurements = re.findall(r"\d+", cleanedInfo)
    # now lets define a dictionary with all the info we want
    MeasurementDict = {
        "Dew Point": mesurements[7],
        "Humidity": mesurements[5],
        "Visibility": mesurements[11],
        "Cloud Coverage": mesurements[10],
    }

    return MeasurementDict
