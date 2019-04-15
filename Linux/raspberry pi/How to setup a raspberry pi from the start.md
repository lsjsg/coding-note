# How to setup a raspberry pi from the start

## install the system

What you need?

An small SD tf card(small card), a laptop, an adaptor for SD card, rasbian image, etcher

The first thing is to go to raspberry pi official website https://www.raspberrypi.org/downloads/raspberry-pi-desktop/ to download the the newest raspberry pi image. Unzip it, please remember where you put it.

Go to website https://www.balena.io/etcher/ to download the software etcher to flash the card.

Run etcher,Select the image you downloaded just now, click flash. this process may take quite a long time. And you may fail to flash it several times. 

If you have a monitor, now you can go to the desktop to setup the system.

## Setup network for PEAP

PEAP is mostly used in companies and Universities, it is more secure than normal WPA.(SUTD turned off port 22 so that we cannot ssh or ping or vnc through SUTD_bot and SUTD_ILP2)

Rasperry pi can find the WIFI using PEAP, but cannot directly connect to it.(others can direct connect) 

Ctrl + Alt + T open the Terminal, type in (you can only use keyboard in the terminal)

type in 

~~~
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
~~~

then add the following lines to the end of the file

SSID is the name of the WIFI, identity is your account and password is your password

~~~
network={
	ssid=""
	key_mgmt=WPA-EAP
	eap=PEAP
	identity=""
	password=""
	phase1="peaplabel=0"
	phase2="auth=MSCHAPV2"
}
~~~

Ctrl + x and enter and enter, saved reboot then the raspberry pi will automatically connect to PEAP wifi

Find out your IP address

eth0 is for wired connection, while wifi0 is for wireless connection

~~~
sudo ifconfig 
~~~

After wifi, the second line find the "inet addr:" this is your IPV4 address

please remember it is you are using ssh or vnc later.

## open ssh and vnc

By default ssh and vnc is closed so we have to manually open it.

Ctrl + Alt + T open the Terminal, type in (you can only use keyboard in the terminal)

~~~
sudo raspi-config
~~~

and use down button go to interface option,  enter, and go to ssh, left button ,enter choose yes, and same as vnc. 

after finish doing this, going down , right button select finish, then reboot.

**ssh and vnc can be used under the same network or the server has a public IP address **

Now you can ssh or use vnc to connect your raspberry pi.

try with 

~~~
ssh pi@   # your IP address
~~~

@is followed by your IP address

to ssh raspberry pi. or using VNC viewer to connect it with GUI desktop.

* For Linux commands tutorial please proceed to https://github.com/lsjsg/coding-note/tree/master/Linux

