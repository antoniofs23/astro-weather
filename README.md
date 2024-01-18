# quick-intro

Scrapes accuweather data for info not normally found on your weather app such as humidity, visibility, dew point, and most importantly for me, **cloud coverage**. Also includes current moon phase data as well as next new moon. All of the info is then conveniently placed on your linux panel. 

![Screenshot from 2024-01-18 13-52-06](https://github.com/antoniofs23/astro-weather/assets/39067846/faa82021-c636-4fd6-bb92-d25d42d7b175)

 usage:
 
- the `manual refresh` bypasses the default 1hour refresh 


## Installation

1. clone this repo to your home directory via:
    `git clone https://github.com/antoniofs23/cloud-coverage.git`
2. In app directory run the `INSTALL.sh` file (first make it executable via `chmod +x INSTALL.sh`)
   
>
>[!IMPORTANT]
>*the install file assumes python is already installed (which it normally is)* if not python3 is required prior to running `INSTALL.sh`. To quickly check if python is installed run `python -V` in your terminal

## running the app
The app should auto-start on login.
However, it can also be run through the `cloud-coverage` terminal command
