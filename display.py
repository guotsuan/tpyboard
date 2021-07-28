def lcd_init():
    import pyb
    from machine import SPI
    import upcd8544

    SPI = pyb.SPI(1)
    #DIN =>SPI(1).MOSI 'X8' data flow (Master out, Slave in)
    #CLK =>SPI(1).SCK  'X6' SPI clock
    RST    = pyb.Pin('X20')
    CE     = pyb.Pin('X19')
    DC     = pyb.Pin('X18')
    LIGHT  = pyb.Pin('X17')
    lcd_5110 = upcd8544.PCD8544(SPI, RST, CE, DC, LIGHT)
    return lcd_5110
