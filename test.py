from newtui import Grid, Widget, Label
from time import sleep

WIDTH = 100
HEIGHT = 30

root = Grid(WIDTH, HEIGHT)
root.render()
# wid = Widget(root,5,5, char=' ')
label = Label(root=root, width=5, height=5, text="Hello", bg="*")
# wid.place_at(0,0,'#')
# wid.pack()
# sleep(1)
# wid.clear()
# wid.pack()
sleep(1)
label.pack()
sleep(1)
