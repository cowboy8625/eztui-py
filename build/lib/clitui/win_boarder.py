from .point import Vector2
from .pixel import Pixel


class BoardStyle:

    ELEMENTS = {
        "hBoarder": [chr(9552), chr(9472), chr(9473)],
        "vBoarder": [chr(9553), chr(9474), chr(9475)],
        "lTee": [chr(9571), chr(9508), chr(9515)],
        "rTee": [chr(9568), chr(9500), chr(9507)],
        "tTee": [chr(9574), chr(9516), chr(9523)],
        "bTee": [chr(9577), chr(9524), chr(9531)],
        "ltCorner": [chr(9556), chr(9581), chr(9487)],
        "rtCorner": [chr(9559), chr(9582), chr(9491)],
        "lbCorner": [chr(9562), chr(9584), chr(9495)],
        "rbCorner": [chr(9565), chr(9583), chr(9499)],
        "lSlope": ["/", "/", "/"],
        "rSlope": ["\\", "\\", "\\"],
        "cross": [chr(9580), chr(9532), chr(9547)],
    }

    def __init__(self, style):
        self.style = style
        self.hBoarder = self.get_char("hBoarder")
        self.vBoarder = self.get_char("vBoarder")
        self.lTee = self.get_char("lTee")
        self.rTee = self.get_char("rTee")
        self.tTee = self.get_char("tTee")
        self.bTee = self.get_char("bTee")
        self.ltCorner = self.get_char("ltCorner")
        self.rtCorner = self.get_char("rtCorner")
        self.lbCorner = self.get_char("lbCorner")
        self.rbCorner = self.get_char("rbCorner")
        self.lSlope = self.get_char("lSlope")
        self.rSlope = self.get_char("rSlope")
        self.cross = self.get_char("cross")

    def get_char(self, name):
        return self.ELEMENTS[name][self.style]


def idx_to_pt(idx, w):
    x = idx % w
    y = idx // w
    return x, y


def pt_to_idx(x, y, w):
    return (y * w) + x


def change_pix(grid, x, y, w, char, bg, fg):
    idx = pt_to_idx(x, y, w)
    grid[y][x] = Pixel(char, idx, fg, bg)


def corners(grid, style, _type, w, tl, tr, bl, br, bg, fg):
    change_pix(grid, tl.x, tl.y, w, _type.ltCorner, bg, fg)
    change_pix(grid, tr.x, tr.y, w, _type.rtCorner, bg, fg)
    change_pix(grid, bl.x, bl.y, w, _type.lbCorner, bg, fg)
    change_pix(grid, br.x, br.y, w, _type.rbCorner, bg, fg)


def horizontal(root, style, _type, tp, bt, w, bg, fg):
    for indices in (tp, bt):
        for idx in indices:
            x, y = idx_to_pt(idx, w)
            change_pix(root.grid, x, y, w, _type.hBoarder, bg, fg)


def vertical(root, style, _type, ls, rs, w, bg, fg):
    for indices in (ls, rs):
        for idx in indices:
            x, y = idx_to_pt(idx, w)
            change_pix(root.grid, x, y, w, _type.vBoarder, bg, fg)


def getstyling(num):
    return BoardStyle(num)


def find_indexes(root):
    W = root.dim.x
    H = root.dim.y
    tl = Vector2(0, 0)
    tr = Vector2(W - 1, 0)
    bl = Vector2(0, H - 1)
    br = Vector2(W - 1, H - 1)
    tp = (i for i in range(1, W - 1))
    bt = (i for i in range(W * H - W + 1, W * H - 1))

    ls = (i for i in range(W, W * H - W, W))

    rs = (i for i in range(W * 2 - 1, W * H - W, W))
    return W, tl, tr, bl, br, tp, bt, ls, rs


def outline(root):
    grid = root.grid
    style = root.style
    _type = getstyling(style[0])
    fg = style[1]
    bg = style[2]
    W, tl, tr, bl, br, tp, bt, ls, rs = find_indexes(root)
    corners(grid, style, _type, W, tl, tr, bl, br, bg, fg)
    horizontal(root, style, _type, tp, bt, W, bg, fg)
    vertical(root, style, _type, ls, rs, W, bg, fg)
