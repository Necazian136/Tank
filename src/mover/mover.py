# noinspection PyUnresolvedReferences
import RPi.GPIO as GPIO


class Mover:
    def __init__(self, mediator):
        self.motor_1 = {'A': 36, 'B': 38, 'E': 40}
        self.motor_2 = {'A': 37, 'B': 35, 'E': 33}

        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.motor_1['A'], GPIO.OUT)
        GPIO.setup(self.motor_1['B'], GPIO.OUT)
        GPIO.setup(self.motor_1['E'], GPIO.OUT)

        GPIO.setup(self.motor_2['A'], GPIO.OUT)
        GPIO.setup(self.motor_2['B'], GPIO.OUT)
        GPIO.setup(self.motor_2['E'], GPIO.OUT)

        mediator.register('up', self.up)
        mediator.register('right', self.right)
        mediator.register('left', self.left)
        mediator.register('down', self.down)
        mediator.register('stop', self.stop)

    def up(self):
        self.forward_motor(self.motor_1)
        self.forward_motor(self.motor_2)

    def right(self):
        self.forward_motor(self.motor_1)
        self.backwards_motor(self.motor_2)

    def left(self):
        self.backwards_motor(self.motor_1)
        self.forward_motor(self.motor_2)

    def down(self):
        self.backwards_motor(self.motor_1)
        self.backwards_motor(self.motor_2)

    def stop(self):
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
        GPIO.output(motor['A'], GPIO.LOW)
        GPIO.output(motor['B'], GPIO.LOW)
        GPIO.output(motor['E'], GPIO.LOW)
