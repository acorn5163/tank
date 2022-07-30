import pigpio
import sys


class Tank:
    def __init__(self):
        self.pi = pigpio.pi()
        print(self.pi.connected)
    
        self.motor_right_F = 13
        self.motor_right_B = 6
        self.motor_left_F = 5
        self.motor_left_B = 9
        self.frequency = 50
        self.range = 100

        self.pi.set_mode(self.motor_right_F,pigpio.OUTPUT)
        self.pi.set_mode(self.motor_right_B,pigpio.OUTPUT)
        self.pi.set_mode(self.motor_left_F,pigpio.OUTPUT)
        self.pi.set_mode(self.motor_left_B,pigpio.OUTPUT)

        self.pi.set_PWM_frequency(self.motor_right_F,self.frequency)
        self.pi.set_PWM_frequency(self.motor_right_B,self.frequency)
        self.pi.set_PWM_frequency(self.motor_left_F,self.frequency)
        self.pi.set_PWM_frequency(self.motor_left_B,self.frequency)

        self.pi.set_PWM_range(self.motor_right_F,self.range)
        self.pi.set_PWM_range(self.motor_right_B,self.range)
        self.pi.set_PWM_range(self.motor_left_F,self.range)
        self.pi.set_PWM_range(self.motor_left_B,self.range)

        print("tankcalled")

        
    def forward(self,dutyright,dutyleft):
        # self.rightF.ChangeDutyCycle(dutyright)
        # self.rightB.ChangeDutyCycle(0)
        # self.leftF.ChangeDutyCycle(dutyleft)
        # self.leftB.ChangeDutyCycle(0)
        self.pi.set_PWM_dutycycle(self.motor_right_F,dutyright)
        self.pi.set_PWM_dutycycle(self.motor_right_B,0)
        self.pi.set_PWM_dutycycle(self.motor_left_F,dutyleft)
        self.pi.set_PWM_dutycycle(self.motor_left_B,0)
        print("-"*20)
        print("tank forwarding")
        print("-"*20)

    def turnright(self,duty):
        #self.rightF.ChangeDutyCycle(dutyright)
        #self.rightB.ChangeDutyCycle(0)
        #self.leftF.ChangeDutyCycle(dutyleft)
        #self.leftB.ChangeDutyCycle(0)
        self.pi.set_PWM_dutycycle(self.motor_right_F,duty)
        self.pi.set_PWM_dutycycle(self.motor_right_B,0)
        self.pi.set_PWM_dutycycle(self.motor_left_F,duty)
        self.pi.set_PWM_dutycycle(self.motor_left_B,0)
        print("-"*20)
        print("tank turning right")
        print("-"*20)

    def turnleft(self,duty,):
        #self.rightF.ChangeDutyCycle(dutyright)
        #self.rightB.ChangeDutyCycle(0)
        #self.leftF.ChangeDutyCycle(dutyleft)
        #self.leftB.ChangeDutyCycle(0)
        self.pi.set_PWM_dutycycle(self.motor_right_F,0)
        self.pi.set_PWM_dutycycle(self.motor_right_B,duty)
        self.pi.set_PWM_dutycycle(self.motor_left_F,0)
        self.pi.set_PWM_dutycycle(self.motor_left_B,duty)
        #print("-"*20)
        #print("tank turning left")
        #print("-"*20)

    def backward(self,dutyright,dutyleft):
        # self.rightF.ChangeDutyCycle(0)
        # self.rightB.ChangeDutyCycle(dutyright)
        # self.leftF.ChangeDutyCycle(0)
        # self.leftB.ChangeDutyCycle(dutyleft)
        self.pi.set_PWM_dutycycle(self.motor_right_B,dutyright)
        self.pi.set_PWM_dutycycle(self.motor_right_F,0)
        self.pi.set_PWM_dutycycle(self.motor_left_B,dutyleft)
        self.pi.set_PWM_dutycycle(self.motor_left_F,0)
        print("-"*20)
        print("tank backwarding")
        print("-"*20)
    
    def stop(self):
        # self.rightF.ChangeDutyCycle(0)
        # self.rightB.ChangeDutyCycle(0)
        # self.leftF.ChangeDutyCycle(0)
        # self.leftB.ChangeDutyCycle(0)
        self.pi.set_PWM_dutycycle(self.motor_right_F,0)
        self.pi.set_PWM_dutycycle(self.motor_right_B,0)
        self.pi.set_PWM_dutycycle(self.motor_left_F,0)
        self.pi.set_PWM_dutycycle(self.motor_left_B,0)
        print("-"*20)
        print("tank stopping")
        print("-"*20)

    
    def close(self):
        self.pi.set_PWM_dutycycle(self.motor_right_F,0)
        self.pi.set_PWM_dutycycle(self.motor_right_B,0)
        self.pi.set_PWM_dutycycle(self.motor_left_F,0)
        self.pi.set_PWM_dutycycle(self.motor_left_B,0)
        print("-"*20)
        print("closing...")
        sys.exit(0)

