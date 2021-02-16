## Steps to create this project

1. Build and test the Pi with various setups:
  - Using a LLC
  - Using a Diode
  - Using simple power supply
  
2. Compile various Python scripts to test:
  - Single color from RGB value (thinking the ZeRGBra will work from Blynk)
  - Pulsating Rainbow
  - Disco
  - Weather
  
3. Write library that includes these defs
  
4. Build Blynk app to control

```python
import libraries

if (blynk sends pin for Zergbra):
  neopixel.fill(red, green, blue)
  
elif (blynk sends pin for rainbow):
  rainbow()

elif (blynk sends pin for disco):
  disco()

elif (blynk sends pin for weather):
  weather()
  
else:
  default()
```
