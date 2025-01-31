import time

class Timer:
    def __init__(self, seconden):
        self.game_time = seconden
        self.seconden = seconden
        self.tijd = 0
        self.running = False
    def start_de_klok(self):
        self.tijd = time.time()
        self.running = True
    def controleer_klok(self):
        if self.running and (time.time() - self.tijd >= 1):
            self.seconden -= 1
            self.tijd = time.time()
        if self.seconden <= 0:
            self.running = False
            self.reset()
    def reset(self):
        self.seconden = self.game_time
        self.tijd = 0



