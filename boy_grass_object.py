from pico2d import *
import random
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)
    def update(self):
        pass

class Boy:
    def __init__(self):
        self.image = load_image('animation_sheet.png')
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.dx = random.randint(-7, 7)
        while (self.dx == 0):
            self.dx = random.randint(-7, 7)
        if self.dx < -3: # 빠르게 왼쪽으로 뛰기
            self.dy = 0
        elif self.dx < 0: # 느리게 왼쪽으로 걷기
            self.dy = 2
        elif self.dx > 3: # 빠르게 오른쪽으로 뛰기
            self.dy = 1
        elif self.dx > 0: # 느리게 오른쪽으로 걷기
            self.dy = 3
    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dx

        if self.x + 20 >= 800:
            self.dy = self.dy - 1
            self.dx = self.dx * -1
        elif self.x - 20 <= 0:
            self.dy = self.dy + 1
            self.dx = self.dx * -1
    def draw(self):
        self.image.clip_draw(self.frame * 100, 100 * self.dy, 100, 100, self.x, self.y)
class Ball:
    def __init__(self):
        self.ballsize = random.randint(0, 1)
        if self.ballsize == 0:
            self.ballsize = 21
            self.image = load_image('ball21x21.png')
        elif self.ballsize == 1:
            self.ballsize = 41
            self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(100, 700), 599
        self.dy = random.randint(3, 8)
        pass
    def update(self):
        self.y = self.y - self.dy
        if self.y <= 70:
            self.dy = 0
        pass
    def draw(self):
        self.image.draw(self.x, self.y)
        pass
def reset_world():
    global running, grass, team, balls, world

    running = True
    world = []

    grass = Grass()
    world.append(grass)
    team = [Boy() for i in range(10)]
    balls = [Ball() for i in range(20)]
    world += team
    world += balls
def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

reset_world()
while running:
    handle_events()
    render_world()
    update_world()
    delay(0.05)

close_canvas()
