from sys import argv

first = argv[1]

if first == "matrix":
    from .matrix_rain import Screen, safe_run

    screen = Screen(fullscreen=True, amount="half")
    safe_run(screen.render)

if first == "creator":
    print("Cowboy8625")

else:
    print(first)
