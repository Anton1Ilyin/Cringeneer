import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)
dac=[26, 19,13,6,5,11,9,10]
leds=[21,20,16,12,7,8,25,24]
GPIO.setup(dac ,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(leds,GPIO.OUT)
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
    for i in range(7, -1, -1):
        value+=2**i
        a=d2b(value)
        GPIO.output(dac,a)
        time.sleep(0.0007)
        if GPIO.input(comp)==0:
            value-=2**i
    return value

#вывод на значения напряжения на leds
def led(v0):
    vi=d2b(v0)
    GPIO.output(leds,vi)
    
try:
    measured_data=[]
    v=0
    start_time=time.time()

    #конденсатор заряжается
    while v<0.97*256:
        v=adc()
        measured_data.append(v)
        led(v)
        print(v)
        
    GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
    
    #конденсатор разряжается
    while v>0.02*256:
        v=adc()
        measured_data.append(v)
        led(v)
        
    end_time=time.time()
    experiment_time=end_time-start_time
    
    #Построение графиков
    plt.plot(range(len(measured_data)), [x*3.3/256 for i in measured_data])
    plt.show()
    
    measured_data_str=[str(item) for item in measured_data]
    
    #создание файлов с данными эксперимента
    with open("data.txt", "w") as file:
        file.write("\n".join(measured_data_str))
    frequency=len(measured_data)/experiment_time
    stroka="Шаг квантования АЦП "+str(3.3/256)+"\n"+"Средняя частота дискретизации"+str(frequency)
    with open("settings.txt", "w") as f:
        f.write(str(3.3/256)+'\n')
        f.write(str(frequency))
        
    print("Время эксперимента", experiment_time)
    print("Период одного измерния",1/frequency)
    print("Средняя частота дискретизации", frequency)
    print("Шаг квантования АЦП", 3.3/256)
finally:
    GPIO.LOW
    GPIO.cleanup()
