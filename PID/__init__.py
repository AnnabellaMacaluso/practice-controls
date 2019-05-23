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

    def output(self):
        return self.output

    def clamp(n, minn, maxn):
        return max(min(maxn, n), minn)

