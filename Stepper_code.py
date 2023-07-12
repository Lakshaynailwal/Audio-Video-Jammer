from time import sleep 
import Rpi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)
GPIO.output(12,0)
GPIO.output(4,0)

MotorDir={
        'forward',
        
        'backward'
}
