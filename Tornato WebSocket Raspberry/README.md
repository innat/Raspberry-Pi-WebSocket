<p align="center">
  <img width="286" height="72" src="http://www.tornadoweb.org/en/stable/_images/tornado.png">
</p>

<h3 align="center">
  Raspberry Pi WebSocket With Tornado
</h3>
<br>

## Task
Creating a WebSockets to control the GPIO pin of Raspberry Pi using the Tornado framework in Python.

## Project Apparatus
### Hardware components:
* Raspberry Pi 3 Model B  (any pi will be OK though)
* Breadboard 
* LED
* Male/Female Jumper Wires
* Resistor 221 ohm

### Software Components:
* Raspberry Pi Raspbian OS
* PUTTY for remotely access

A clean basic knowledge required of
* Python 3x
* HTML , CSS , JavaScript
* Tornado framework


## Working Steps

We will access our raspberry pi remotely by using Putty which is a SSH and telnet client. First Download [Putty](https://www.putty.org/) and install it on winodws. Connect your Putty to Raspberry Pi so that we can access or navigate pi directory via terminal. Please do a google search if you have trouble for connecting your putty to raspberry pi.

After connecting with raspberry pi via putty open a session and proceed to rasbian directory.

### Pacakge Installation:
Python is already built-in in Rasbian OS. All we need now is to install [tornado](http://www.tornadoweb.org/en/stable/) package manually. We also need to install the RPi.GPIO package to interact with Rasberry pi GPIO pins with python. Run the following command for gradually for installing all of them properly

```shell
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install rpi.gpio
sudo pip install tornado
```

### Experimental Setup
11 , 13 and 16 , 18 are set up Rapberry GPIO Pins and use 39 as our Ground port though you may use any.The set up connection layout ar given below.

```shell
GPIO PIN 11  ->  (ve+) RED   LED(ve-)   -> Ground
GPIO PIN 13  ->  (ve+) BLUE  LED(ve-)   -> Ground
GPIO PIN 16  ->  (ve+) GRAY  LED(ve-)   -> Ground
GPIO PIN 18  ->  (ve+) WHITE LED(ve-)   -> Ground 
```
Check the connection whether LED get power or not. Create `nano test_led.py` and type following piece of python code there.

```python

# including pacakges
import RPi.GPIO as GPIO
import time

#Set GPIO pins as outputs
GPIO.setmode(GPIO.BOARD)

# set pin 11 and 13 as Output
# we only test two pins here
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

#Switch GPIO pins ON
GPIO.output(11, True)
GPIO.output(13, True)

#make 5 seconds delay 
time.sleep(5)

#Switch GPIO pins OFF
GPIO.output(11, False)
GPIO.output(13, False)

#Reset GPIO pins to their default state
#note : very important
GPIO.cleanup()
```

Save your file by pressing simultanuely `Cytl + X` and 'Y' to save it , finish with press enter. Now it should create properly. Run the code by giving following command -

`sudo python test_led.py` 

and hit enter. Your led shuld blink for five second.

## Run Project
First download this repository `git clone https://github.com/iphton/Raspberry-Pi-WebSocket.git` or simply download locally. After download the repo extract it and run the python file as following.

`sudo python server.py`

Tornado server will be started shortly.It will short from port 80 as we programmed.

![puttty](https://user-images.githubusercontent.com/17668390/39704364-eb60172e-51bf-11e8-9f01-dc43f56fe7fb.JPG)

Now from your pi browser or from any brower in pc , go folowing -

> ip_address:80

This ip address is unique and it's basically your raspberry pi ip address and following colon mark 80 is the given port number from where our server will started from our pc. After entering this port following page will be opened.

![connected](https://user-images.githubusercontent.com/17668390/39704460-3b452496-51c0-11e8-927e-62d24d85ed33.JPG)

Now we can control GPIO pin from our brower by making a web socket.

---
Regards

**World of Void**
