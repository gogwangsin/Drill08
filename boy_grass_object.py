from pico2d import *
import random

# Game object class here

class Grass:
    def __init__(self): # 생성자 Constructor
        self.image = load_image('grass.png')

    def draw(self): # 멤버 함수는 항상 첫번째 인자가 self 이어야 한다.
        self.image.draw(400, 30)

    def update(self): pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0, 7) # 싱크를 잘 맞춰서 만들어야 한다.
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class SmallBall: # 90 + 21 
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599
        self.image = load_image('ball21x21.png')

    def update(self):
        self.velocity = random.randint(3, 20)
        if self.y - self.velocity >= 40 + 21:
            self.y -= self.velocity
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

class BigBall: # 90 + 41 
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599
        self.image = load_image('ball41x41.png')

    def update(self):
        self.velocity = random.randint(3, 20)
        if self.y - self.velocity >= 50 + 21:
            self.y -= self.velocity
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
         

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code
def reset_world(): # 맨 처음 초기화 할 때 '잔디 객체 생성'
    global running
    global grass
    global team
    global world

    running = True
    world = []

    grass = Grass() # 객체 이름 = 클래스 이름
    world.append(grass) # 리스트에 원소 넣기

    team = [Boy() for i in range(10)]
    world += team # 리스트 합치기

    # small_ball = [ SmallBall() for i in range(10)] 
    # world += small_ball

    big_ball = [ BigBall() for i in range(10)]
    world += big_ball


def update_world():
    grass.update()
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code
close_canvas()
