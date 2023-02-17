# Python Whoopee Cushion
Python flask web server with a button a few sounds to play fart noises from the server.
 - This project is meant for a Raspberry Pi, but most Linux distributions will work
 - This was mostly written by ChatGPT

![App Screenshot](/whoopeeCushionScreen.png)

# Get started

## Install Python and Pip
You can get Python from the [official website](https://www.python.org/downloads/)

### On Raspberry Pi
Install Python 3:
```bash
sudo apt update
sudo apt install python3
```

Install Pip:
```bash
sudo apt update
sudo apt install python3-pip
```

## Install Python dependencies
Once Python is installed, install necessary dependencies (`flask` and `pygame`) with:
```bash
py -m pip install flask pygame
```

## Run the web server
Run the web server with `py main.py`


# Attributions

## Audio files
Fart audio files from the Raspberry Pi foundation's [Whoopi cushion project](https://projects.raspberrypi.org/en/projects/whoopi-cushion)