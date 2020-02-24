import time
from clitui import Menu, getchar, fg_by, bg_by, safe_run, is_pressed, clear


def foo(x, y, z):
    return x + y + z


FG_CYAN = fg_by(0, 160, 160)

main_menu = Menu("Main Menu", x=25, y=5, border=True, btype=2)
options_menu = Menu("Options Menu")
key_controls = Menu("Key Controler")

main_menu.background_color((50, 0, 0))

main_menu.add("New Game", 0).font_color_for(0, (0, 255, 0))
main_menu.add("Load", 1).font_color_for(1, FG_CYAN)
main_menu.add("Save", 2).font_color_for(2, "Cyan")
main_menu.add("Options", 3).submenu(3, options_menu)
main_menu.add("Exit", 4).add_action(4, exit)

options_menu.add("Sound", 0)
options_menu.add("Controls", 1).submenu(1, key_controls)

key_controls.add("Key0", 0)
key_controls.add("Key1", 1)
key_controls.add("Key2", 2)
key_controls.add("Key3", 3)

main_menu.create()


def main():
    last = time.time()
    while True:
        if time.time() - last > 0.5:
            clear()
            last = time.time()
        key = getchar()
        main_menu.draw()
        action = main_menu.move_curser(key)
        if action is not None:
            action()

        if is_pressed("ESC", key):
            exit()


# main()
safe_run(main)
