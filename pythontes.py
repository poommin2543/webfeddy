from machine import Pin
from time import sleep_ms, ticks_ms, ticks_diff, time

pinA = Pin(32, Pin.IN)
pinB = Pin(33, Pin.IN)
x = 0
t = 0.00001
c = 0


def count(t):
    global x
    global c
    x = x + 1
    if pinB.value() == 1:
        c = c+1
    else:
        c = c-1


pinA.irg(trigger=Pin.IRQ_RISING, handler=count)

while True:
    if x == 0:
        start = ticks_ms()
    elif x >= 600:
        t = ticks_diff(ticks_ms(), start)
        x = 0
        start = ticks_ms()
    if c >= 600 or c <= -600:
        c = 0
    if c >= 1:
        print((c/600) * 360)
    elif c <= 0:
        print(((600+c) / 600) * 360)

    print("speed", (60)/(t/1000), " rpm")
    sleep_ms(50)
