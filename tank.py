import RPi.GPIO as GPIO
import sys



class Tank:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.motor_right_F = 13
        self.motor_right_B = 6
        self.motor_left_F = 5
        self.motor_left_B = 9
        self.duty = 80

        GPIO.setup(self.motor_right_F, GPIO.OUT)
        GPIO.setup(self.motor_right_B, GPIO.OUT)
        GPIO.setup(self.motor_left_F, GPIO.OUT)
        GPIO.setup(self.motor_left_B, GPIO.OUT)
    
        #それぞれをPWMに設定
        self.rightF = GPIO.PWM(self.motor_right_F,50)
        self.rightB = GPIO.PWM(self.motor_right_B,50)
        self.leftF = GPIO.PWM(self.motor_left_F,50)
        self.leftB = GPIO.PWM(self.motor_left_B,50)

        self.rightF.start(0)
        self.rightB.start(0)
        self.leftF.start(0)
        self.leftB.start(0)
        print("tankcalled")

        
    def forward(self,dutyright,dutyleft):
        self.rightF.ChangeDutyCycle(dutyright)
        self.rightB.ChangeDutyCycle(0)
        self.leftF.ChangeDutyCycle(dutyleft)
        self.leftB.ChangeDutyCycle(0)
        print("-"*20)
        print("tank forwarding")
        print("-"*20)

    #def turnright(self,dutyright,dutyleft):
        #self.rightF.ChangeDutyCycle(dutyright)
        #self.rightB.ChangeDutyCycle(0)
        #self.leftF.ChangeDutyCycle(dutyleft)
        #self.leftB.ChangeDutyCycle(0)
        #print("-"*20)
        #print("tank turning right")
        #print("-"*20)

    #def turnleft(self,dutyright,dutylight):
        #self.rightF.ChangeDutyCycle(dutyright)
        #self.rightB.ChangeDutyCycle(0)
        #self.leftF.ChangeDutyCycle(dutyleft)
        #self.leftB.ChangeDutyCycle(0)
        #print("-"*20)
        #print("tank turning left")
        #print("-"*20)

    def backward(self,dutyright,dutyleft):
        self.rightF.ChangeDutyCycle(0)
        self.rightB.ChangeDutyCycle(dutyright)
        self.leftF.ChangeDutyCycle(0)
        self.leftB.ChangeDutyCycle(dutyleft)
        print("-"*20)
        print("tank backwarding")
        print("-"*20)
    
    def stop(self):
        self.rightF.ChangeDutyCycle(0)
        self.rightB.ChangeDutyCycle(0)
        self.leftF.ChangeDutyCycle(0)
        self.leftB.ChangeDutyCycle(0)
        print("-"*20)
        print("tank stopping")
        print("-"*20)

    
    def close(self):
        self.rightF.ChangeDutyCycle(0)
        self.rightB.ChangeDutyCycle(0)
        self.leftF.ChangeDutyCycle(0)
        self.leftB.ChangeDutyCycle(0)
        print("-"*20)
        print("closing...")
        GPIO.cleanup()
        sys.exit(0)

