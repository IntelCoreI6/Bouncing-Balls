import time

class Timer:
    def __init__(self, seconden):
        self.game_time = seconden
        self.seconden = seconden
        self.tijd = 0
    def start_de_klok(self):
        self.tijd = time.time()
    def controleer_klok(self):
        if time.time() - self.tijd >= 1:
            self.seconden -= 1
            self.tijd = time.time()
        if self.seconden <= 0:
            self.seconden = 0  # Ensure the timer does not go negative
    def reset(self):
        self.seconden = self.game_time
        self.tijd = 0



