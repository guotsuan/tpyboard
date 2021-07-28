# main.py -- put your code here!
#main.py
import pyb
import upcd8544
from machine import SPI,Pin
from pyb import UART
from enviroment import read_t_h_l
from display import lcd_init
lcd_5110 =  lcd_init()

N2 = Pin('Y3', Pin.OUT_PP)
N1 = Pin('Y6', Pin.OUT_PP)
N1.low()
pyb.delay(4000)
N1.high()

while True:
    t, h, l = read_t_h_l()
    lcd_5110.lcd_write_string('Temp:',0,0)
    lcd_5110.lcd_write_string(str(t),0,1)
    lcd_5110.lcd_write_string('Humidity:',0,2)
    lcd_5110.lcd_write_string(str(h),0,3)
    lcd_5110.lcd_write_string('Luminosity:',0,4)
    lcd_5110.lcd_write_string(str(l),0,5)
