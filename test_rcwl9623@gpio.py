
import utime
from machine import Pin

echo=Pin(18,Pin.IN)
trig=Pin(26,Pin.OUT)

def getDistance():
    trig.low()
    utime.sleep_us(10)
    trig.high()
    utime.sleep_us(10)
    trig.low()
    
    while echo.value()==0:
        start = utime.ticks_us()
    while echo.value()==1:
        end=utime.ticks_us()
    ret=(end-start)*((342.62*100)/1000/1000)/2
    return ret

while True:
    distance=getDistance()
    print("距离={:7.2f}(厘米)".format(distance),end='\r')
    utime.sleep(0.1)