import game_framework
from pico2d import *
import game_world
from boy import Boy
from grass import Grass
import ball_item


item_mode = False
selected_item = ball_item.DEFAULT
item_select_image = None


def select_item(key):
    if key == SDLK_0:
        return ball_item.NONE
    if key == SDLK_1:
        return ball_item.SMALL_BALL
    if key == SDLK_2:
        return ball_item.BIG_BALL
    return None


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
            item = select_item(event.key)
            if item is not None:
                selected_item = item
        elif not item_mode:
            boy.handle_event(event, selected_item)

def init():
    global boy, item_mode, selected_item, item_select_image

    item_mode = False
    selected_item = ball_item.DEFAULT
    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)
    item_select_image = load_image('item_select.png')

def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    if item_mode:
        item_select_image.draw(get_canvas_width() // 2,
                               get_canvas_height() // 2)
    update_canvas()

def finish():
    game_world.clear()


def pause():
    pass


def resume():
    pass
