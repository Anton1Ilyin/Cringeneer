import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)
dac=[26, 19,13,6,5,11,9,10]
leds=[21,20,16,12,7,8,25,24]
GPIO.setup(dac ,GPIO.OUT)
[GPIO.setup(x,GPIO.OUT) for x in leds]
comp=4
troyka=17
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
#перевод из десятичной в двоичную
def d2b(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
#измерение напряжения на выходе тройка-модуля
def adc():
    value=0
    v=0
    for i in range(8):
        v=value+2**(7-i)
        if v<256:
            a=d2b(v)
        GPIO.output(dac,v)
        time.sleep(0.0007)
        if GPIO.input(comp)==1:
            value=v
    return value
#вывод на значения напряжения на leds
def led(v0):
    v=d2b(v0)
    [GPIO.output(leds[x],v[x]) for x in range(len(leds))]
try:
    measured_data=[]
    start_time=time.time()
    GPIO.output(troyka, 1)
    vi=adc()
    while (vi<0.97*3.3):
        measured_data.append(vi)
        vi=adc()
        led(vi)
    GPIO.output(troyka,0)
    vi=adc()
    while (vi>0.02*3.3):
        measured_data.append(vi)
        vi=adc()
        led(vi)
    end_time=time.time()
    experiment_time=end_time-start_time
    plt.scatter(range(len(measured_data)), measured_data)
    plt.show()
    measured_data_str=[str(item) for item in measured_data]
    with open("data.txt", "w") as file:
        file.write("\n".join(measured_data_str))
    frequency=len(measured_data)/experiment_time
    stroka="Шаг квантования АЦП "+str(3.3/256)+"\n"+"Средняя частота дискретизации"+str(frequency)
    with open("settings.txt", "w") as f:
        f.write(stroka)
    print("Время эксперимента", experiment_time)
    print("Период одного измерния",1/frequency)
    print("Средняя частота дискретизации", frequency)
    print("Шаг квантования АЦП", 3.3/256)
finally:
    GPIO.LOW
    GPIO.cleanup()
