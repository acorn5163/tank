import pigpio
import sys

class Tank:

    def __init__(self):
        
        pi = pigpio.pi()
        
        self.motor_right_F = 13
        self.motor_right_B = 6
        self.motor_left_F = 5
        self.motor_left_B = 0
        self.frequency = 50
        self.range = 100

        pi.set_mode(self.motor_right_F,pigpio.OUTPUT)
        pi.set_mode(self.motor_right_B,pigpio.OUTPUT)
        pi.set_mode(self.motor_left_F,pigpio.OUTPUT)
        pi.set_mode(self.motor_left_B,pigpio.OUTPUT)

        pi.set_PWM_frequency(self.motor_right_F,self.frequency)
        pi.set_PWM_frequency(self.motor_right_B,self.frequency)
        pi.set_PWM_frequency(self.motor_left_F,self.frequency)
        pi.set_PWM_frequency(self.motor_left_B,self.frequency)

        pi.set_PWM_range(self.motor_right_F,self.range)
        pi.set_PWM_range(self.motor_right_B,self.range)
        pi.set_PWM_range(self.motor_left_F,self.range)
        pi.set_PWM_range(self.motor_left_B,self.range)

        print("tankcalled")

        
    def forward(self,dutyright,dutyleft):
        # self.rightF.ChangeDutyCycle(dutyright)
        # self.rightB.ChangeDutyCycle(0)
        # self.leftF.ChangeDutyCycle(dutyleft)
        # self.leftB.ChangeDutyCycle(0)
        pi.set_PWM_dutycycle(self.motor_right_F,dutyright)
        pi.set_PWM_dutycycle(self.motor_right_B,0)
        pi.set_PWM_dutycycle(self.motor_left_F,dutyleft)
        pi.set_PWM_dutycycle(self.motor_left_B,0)
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
        # self.rightF.ChangeDutyCycle(0)
        # self.rightB.ChangeDutyCycle(dutyright)
        # self.leftF.ChangeDutyCycle(0)
        # self.leftB.ChangeDutyCycle(dutyleft)
        pi.set_PWM_dutycycle(self.motor_right_B,dutyright)
        pi.set_PWM_dutycycle(self.motor_right_F,0)
        pi.set_PWM_dutycycle(self.motor_left_B,dutyleft)
        pi.set_PWM_dutycycle(self.motor_left_F,0)
        print("-"*20)
        print("tank backwarding")
        print("-"*20)
    
    def stop(self):
        # self.rightF.ChangeDutyCycle(0)
        # self.rightB.ChangeDutyCycle(0)
        # self.leftF.ChangeDutyCycle(0)
        # self.leftB.ChangeDutyCycle(0)
        pi.set_PWM_dutycycle(self.motor_right_F,0)
        pi.set_PWM_dutycycle(self.motor_right_B,0)
        pi.set_PWM_dutycycle(self.motor_left_F,0)
        pi.set_PWM_dutycycle(self.motor_left_B,0)
        print("-"*20)
        print("tank stopping")
        print("-"*20)

    
    def close(self):
        pi.set_PWM_dutycycle(self.motor_right_F,0)
        pi.set_PWM_dutycycle(self.motor_right_B,0)
        pi.set_PWM_dutycycle(self.motor_left_F,0)
        pi.set_PWM_dutycycle(self.motor_left_B,0)
        print("-"*20)
        print("closing...")
        GPIO.cleanup()
        sys.exit(0)

