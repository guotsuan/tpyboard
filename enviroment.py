def read_t_h_l():
    import pyb
    from sht20 import SHT20
    from machine import Pin

    ds = SHT20(1)
    ads = pyb.ADC(Pin('Y12'))
    pyb.delay(2000)
    a=ads.read()
    a=a/100
    a=33-a
    pyb.delay(1000)
    H=ds.TEMP()
    pyb.delay(1000)
    S=ds.TEMP1()
    H=125*H/256-6
    S=175.72*S/256-46.85
    print("Temp, Humidity, Luminosity: ", S, H, a)

    return (S, H, a)
