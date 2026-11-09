import game_framework
from pico2d import *
import game_world
from boy import Boy
from grass import Grass
import ball_item


item_mode = False
selected_item = ball_item.DEFAULT


def handle_events():
    global item_mode, selected_item

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            item_mode = not item_mode
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            import title_mode
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            import pause_mode
            game_framework.push_mode(pause_mode)
        elif item_mode and event.type == SDL_KEYDOWN:
            if event.key == SDLK_0:
                selected_item = ball_item.NONE
            elif event.key == SDLK_1:
                selected_item = ball_item.SMALL_BALL
            elif event.key == SDLK_2:
                selected_item = ball_item.BIG_BALL
        elif not item_mode:
            boy.handle_event(event, selected_item)

def init():
    global boy

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)

def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()


def pause():
    pass


def resume():
    pass
