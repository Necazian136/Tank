import RPi.GPIO as GPIO


class TankManager:
    def __init__(self):
        self.motor_1 = {'A': 36, 'B': 38, 'E': 40}
        self.motor_2 = {'A': 37, 'B': 35, 'E': 33}

        GPIO.setup(self.motor_1['A'], GPIO.OUT)
        GPIO.setup(self.motor_1['B'], GPIO.OUT)
        GPIO.setup(self.motor_1['E'], GPIO.OUT)

        GPIO.setup(self.motor_2['A'], GPIO.OUT)
        GPIO.setup(self.motor_2['B'], GPIO.OUT)
        GPIO.setup(self.motor_2['E'], GPIO.OUT)

    def action(self, action):
        if action == 'up':
            self.forward_motor(self.motor_1)
            self.forward_motor(self.motor_2)

        if action == 'right':
            self.forward_motor(self.motor_1)
            self.backwards_motor(self.motor_2)

        if action == 'left':
            self.backwards_motor(self.motor_1)
            self.forward_motor(self.motor_2)

        if action == 'down':
            self.backwards_motor(self.motor_1)
            self.backwards_motor(self.motor_2)

        if action == 'stop':
            self.motor_stop(self.motor_1)
            self.motor_stop(self.motor_2)

    def forward_motor(self, motor):
        GPIO.output(motor['A'], GPIO.HIGH)
        GPIO.output(motor['B'], GPIO.LOW)
        GPIO.output(motor['E'], GPIO.HIGH)

    def backwards_motor(self, motor):
        GPIO.output(motor['A'], GPIO.LOW)
        GPIO.output(motor['B'], GPIO.HIGH)
        GPIO.output(motor['E'], GPIO.HIGH)

    def motor_stop(self, motor):
        GPIO.output(motor['E'], GPIO.HIGH)
