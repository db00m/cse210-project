from core.actor import Actor
from game import constants
import time


class Timer(Actor):
    def __init__(self):
        super().__init__()
        self.center_x = 50
        self.center_y = constants.SCREEN_HEIGHT - 30
        self.start_time = time.time()
        self.stop_time = 0.0
        self.elapsed_time = ""
    
    # Will be called when the game starts
    def start_timer(self):
        self.start_time = time.time()
    
    # Will be called when the maze is solved
    def stop_timer(self):
        self.stop_time = time.time()

    # Will be called every time things update
    def update(self):
        self.calculate_time()

    # Will be called from update
    def calculate_time(self):
        current_time = time.time()
        elapsed = int(current_time - self.start_time)
        if elapsed < 60:
            self.elapsed_time = f"{elapsed}"
        elif elapsed >= 60:
            minutes = elapsed // 60
            seconds = elapsed % 60
            if seconds <= 9:
                self.elapsed_time = f"{minutes}:0{seconds}"
            else:
                self.elapsed_time = f"{minutes}:{seconds}"