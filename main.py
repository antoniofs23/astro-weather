import getWeatherData as gwd
from threading import Thread
import signal
import gi
import os
import time

gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")
from gi.repository import Gtk, AppIndicator3, GObject

# change the working directory when script is run through command-line
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)

# see if link text exists
target_url = gwd.pop_up_win()


class Indicator:
    def __init__(self):
        self.app = "cloud-coverage"
        iconpath = os.path.abspath("clouds.svg")
        self.indicator = AppIndicator3.Indicator.new(
            self.app, iconpath, AppIndicator3.IndicatorCategory.OTHER
        )
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.create_menu())
        # add thread
        self.update = Thread(target=self.update_battery_status)
        # dameonize
        self.update.setDaemon(True)
        self.update.start()

    def create_menu(self):
        menu = Gtk.Menu()

        weather_data = gwd.ScrapeWeather(target_url)
        label = list(weather_data.keys())
        values = list(weather_data.values())
        units = ["°F", "%", " mi", "%"]

        # add devices + battery%s
        for num in range(len(label)):
            item_model = Gtk.MenuItem(label[num] + ": " + values[num] + units[num])
            menu.append(item_model)

        # add a separator between weather data and reload button
        menu_sep = Gtk.SeparatorMenuItem()
        menu.append(menu_sep)

        # manual_refresh incase user doesn't want to wait an hour
        item_manual_refresh = Gtk.MenuItem("manual refresh")
        item_manual_refresh.connect("activate", self.manual_refresh)
        menu.append(item_manual_refresh)

        menu.show_all()
        return menu

    def manual_refresh(self, source):
        GObject.idle_add(
            self.indicator.set_menu,
            self.create_menu(),
            priority=GObject.PRIORITY_DEFAULT,
        )

    def update_battery_status(self):
        while True:
            time.sleep(3600)  # updates every hour
            # apply interface update
            GObject.idle_add(
                self.indicator.set_menu,
                self.create_menu(),
                priority=GObject.PRIORITY_DEFAULT,
            )


Indicator()
GObject.threads_init()
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()
