# temperature-thingspeak
Temperature monitoring with  ThingSpeak

[![Build Status](https://drone.io/github.com/wuttinunt/temperature-thingspeak/status.png)](https://drone.io/github.com/wuttinunt/temperature-thingspeak/latest)


## Clone repository
```bash
git clone https://github.com/wuttinunt/temperature-thingspeak.git
cd temperature-thingspeak
```

## Edit config file ```w1-gpio```
```bash
sudo nano /boot/config.txt
```
Look at ```#dtoverlay=w1-gpio``` and uncomment ```dtoverlay=w1-gpio```

## Connect Raspberry Pi with DS18B20

![RasPi](image.png?raw=true "RasPi")

## Install DS18B20 and Kernel Module
```bash
sudo pip install ds18b20
sudo modprobe w1-gpio
sudo modprobe w1-therm
```
Look some Directory ``` /sys/bus/w1/devices ``` you'll see directory 28-XXXXXXXXXXX
try:
```bash
cat/sys/bus/w1/devices/28-XXXXXXXXXXX/w1_slave
```
you'll see some value it's ready to work
if you don't see Directory ensure you connect Raspberry Pi with DS18B20 already.

## Run

```bash
sudo python temperature.py
```

## Read data by ThingSpeak
This is my ThingSpeak account you can register account free from www.thingspeak.com and setting somthing but it easy
go to websit https://thingspeak.com/channels/113862



