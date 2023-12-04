import dearpygui.dearpygui as dpg
import random


def help():
    dpg.create_context()
    dpg.create_viewport(title='Barnsley fern', width=900, height=600)


    def barnsley_fern(size=1, color=(0, 255, 0, 255)):
        x, y = 0, 0
        for _ in range(10000):
            r = random.random()
            if r < 0.01:
                x, y = 0, 0.16 * y
            elif r < 0.86:
                new_x = 0.85 * x + 0.04 * y
                new_y = -0.04 * x + 0.85 * y + 1.6
                x, y = new_x, new_y
            elif r < 0.93:
                new_x = 0.2 * x - 0.26 * y
                new_y = 0.23 * x + 0.22 * y + 1.6
                x, y = new_x, new_y
            else:
                new_x = -0.15 * x + 0.28 * y
                new_y = 0.26 * x + 0.24 * y + 0.44
                x, y = new_x, new_y
            dpg.draw_circle((int(50 * x) + 300, int(50 * y) + 50), size, fill=color, color=color, parent='root')


    def draw():
        dpg.delete_item('root', children_only=True)
        barnsley_fern(
            size=dpg.get_value('size'),
            color=dpg.get_value('color')
        )


    with dpg.window(tag='controls', label='controls', pos=(450, 10), width=400):
        dpg.add_text('Fractal settings:')
        dpg.add_slider_int(tag='size', label='size', default_value=1, min_value=1, max_value=10, callback=draw)
        dpg.add_color_edit(tag='color', label='color', default_value=[0, 255, 0], callback=draw)

        dpg.configure_item('controls', no_close=True)

    with dpg.window(tag="Window"):
        with dpg.drawlist(tag='canvas', width=720, height=600):
            with dpg.draw_node(tag='root'):
                draw()

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Window", True)

    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()

    dpg.destroy_context()
