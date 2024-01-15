# quick-intro

Scrapes accuweather data for info not normally found on your weather app such as humidity, visibility, dew point, and most importantly for me, **cloud coverage**. All of the info is then conveniently placed on your linux panel. 

![Screenshot from 2024-01-12 18-45-05](https://github.com/antoniofs23/cloud-coverage/assets/39067846/8de98a77-fe12-4957-a798-efd7247928bb)

 usage:
 
- the `manual refresh` bypasses the default 1hour refresh 


## Installation

1. clone this repo to your home directory via:
    `git clone https://github.com/antoniofs23/cloud-coverage.git`
2. In app directory run the `INSTALL.sh` file
3. - **before running need to make the file executable via `chmod +x INSTALL.sh`**
   
>
>[!IMPORTANT]
>*the install file assumes python is already installed (which it normally is)* if not python3 is required prior to running `INSTALL.sh`. To quickly check if python is installed run `python -V` in your terminal

## running the app
The app should auto-start on login.
However, it can also be run through the `cloud-coverage` terminal command
