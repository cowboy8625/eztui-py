class Char:
    shade_one            = chr(9617) # ░
    shade_two            = chr(9618) # ▒
    shade_three          = chr(9619) # ▓
    shade_four           = chr(9608) # █
    top_half             = chr(9600) #  ▀
    bottom_half          = chr(9605) # ▄ 
    one                  = chr(9624) #  ▘
    two                  = chr(9629) # ▝
    three                = chr(9622) #  ▖
    four                 = chr(9623) # ▗
    two_three_four       = chr(9630) #  ▟
    one_three_four       = chr(9625) # ▙
    one_two_three        = chr(9627) #  ▛
    one_two_four         = chr(9628) # ▜
    one_four             = chr(9626) #  ▚
    two_three            = chr(9630) # ▞
    middle               = chr(9632) #  ■

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


