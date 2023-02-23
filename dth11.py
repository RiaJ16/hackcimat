import Adafruit_DHT
import time
 
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
 
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temperatura= {} ºC \tHumedad= {}%".format(temperature, humidity))
    else:
        print("Sensor no encontrado")
    time.sleep(1)
