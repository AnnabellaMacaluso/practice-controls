import RPi.GPIO as GPIO
import time


class PID:
    error = 0
    dt = 0.01
    accumulated_error = 0
    last_error = 0

    kp = 0
    ki = 0
    kd = 0

    output = 0

    def __init__(self, P:float, I:float, D:float, dt):
        self.kp = P
        self.ki = I
        self.kd = D
        self.dt = dt

    def calculations(self, desired_pos, position):
        global dt
        global accumulated_error
        global last_error
        global error
        global kp, ki, kd
        global output

        error = desired_pos - position

        proportional = kp * error
        integral = ki * accumulated_error
        derivative = kd * ((error - last_error) / dt)

        output = proportional + integral + derivative
        output = self.clamp(output, -100, 100)

        last_error = error
        accumulated_error += self.error * dt

        return output

    def get_output(self):
        return self.output

    def clamp(n, minn, maxn):
        return max(min(maxn, n), minn)


GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN) #encoder
GPIO.setup(15, GPIO.IN)
GPIO.setup(24, GPIO.OUT) #motor
GPIO.setup(23, GPIO.OUT)
GPIO.setup(25, GPIO.OUT) #pwm

p = GPIO.PWM(25, 490)
GPIO.output(24, GPIO.HIGH)
GPIO.output(23, GPIO.LOW)
p.start(0)


counts = 0
Encoder_A_old = 0
Encoder_B_old = 0

P = float(10/6) #random filler values
I = 0
D = 0
dt = 0.001
desired_pos = 60

def encodercount():
    global counts
    global Encoder_A
    global Encoder_B
    global Encoder_A_old
    global Encoder_B_old
    global error

    Encoder_A = GPIO.input(15)
    Encoder_B = GPIO.input(14)

    if (Encoder_A ^ Encoder_B_old == 1):
        counts += 1

    else:
        counts -= 1

    # if (Encoder_A == 1 and Encoder_B_old == 0) or (Encoder_A == 0 and Encoder_B_old == 1):
    #     # this will be clockwise rotation
    #     counts += 1
    #
    # elif (Encoder_A == 1 and Encoder_B_old == 1) or (Encoder_A == 0 and Encoder_B_old == 0):
    #     # this will be counter-clockwise rotation
    #     counts -= 1
    #
    # else:
    #     # this will be an error as well
    #     error += 1

    Encoder_A_old = Encoder_A
    Encoder_B_old = Encoder_B


GPIO.add_event_detect(14, GPIO.BOTH, callback=encodercount)  # Encoder A
GPIO.add_event_detect(15, GPIO.BOTH, callback=encodercount)  # Encoder B


# class mythread(threading.Thread):
#
#     def run(self):
#         while True:
#             encodercount()
#             time.sleep(0.0000001)
#
#
# thread1 = mythread()
# thread1.daemon = True
# thread1.start()

controller = PID(P, I, D, dt)

while True:
    position = (counts / 2048.0) * 360
    print(position)
    controller.calculations(desired_pos, position)

    if (controller.output > 0):

        GPIO.output(24, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)

    else:

        GPIO.output(24, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)

    p.ChangeDutyCycle = abs(controller.output)

    time.sleep(dt)




