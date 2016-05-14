#!/usr/bin/env python
# -*- coding: utf-8 -*-
import httplib, urllib
import urllib2
from time import sleep
from ds18b20 import DS18B20

def main():
    sensor = DS18B20()
    
    while True:
        temperatures = sensor.get_temperatures([DS18B20.DEGREES_C, DS18B20.DEGREES_F, DS18B20.KELVIN])

        print("Kelvin: %f" % temperatures[2])
        print("Degrees Celsius: %f" % temperatures[0])
        print("Degrees Fahrenheit: %f" % temperatures[1])
        
        #sleep(5)

   	baseURL = 'https://api.thingspeak.com/update?api_key='  #api_key=your_api_key
	
        try:
            	f = urllib.urlopen(baseURL +
                                   "&field1=%f&field2=%f&field3=%f" % (temperatures[0],temperatures[2],temperatures[1]))
                print 'Entries : ' + f.read()
            	print("=====================================")
            	f.close()
            	sleep(15)
        except:

                print'exit.'
         	    break;
        

if __name__ == "__main__":
    main()

