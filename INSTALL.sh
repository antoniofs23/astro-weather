#!/bin/bash
# an install file that:
# 1. creates a terminal alias
# 2. installs python dependencies
# 3. sets app as a start-up process

# Start Install
# 1. Create a terminal alias in .bashrc
echo "alias astro-weather='python3 ~/astro-weather/main.py &'" >> ~/.bashrc

# 2. Install python dependencies
pip install -r requirements.txt
sudo apt install libgirepository1.0-dev

# 3. set up as start-up process
# get username 
name=$(whoami)
#build the .desktop file
cd ~/.config/autostart/
cat <<EOT >> astro-weather.desktop
[Desktop Entry]
Type=Application
Path=/home/$name/astro-weather/
Exec=python3 main.py
Terminal=false
Icon=htop
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=astro-weather
Comment[en_US]=runs astro-weather
EOT
