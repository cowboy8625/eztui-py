info = "http://ascii-table.com/ansi-escape-sequences-vt-100.php"
info2 = "http://ascii-table.com/ansi-escape-sequences.php"

def Fore_Back(text, fore="white", back="black"):
    if hasattr(FG, fore):
        return f"{FG.__dir__[{fore}]}{text}{FG.reset}"
    else:
        raise "Not the Right Color"


class FontColor:
    red            = "\033[31m"
    green          = "\033[32m"
    yellow         = "\033[33m"
    blue           = "\033[34m"
    magenta        = "\033[35m"
    cyan           = "\033[36m"
    white          = "\033[37m"
    bright_black   = "\033[90m"
    bright_red     = "\033[91m"
    bright_green   = "\033[92m"
    bright_yellow  = "\033[93m"
    bright_blue    = "\033[94m"
    bright_magenta = "\033[95m"
    bright_cyan    = "\033[96m"
    bright_white   = "\033[97m"
    reset          = "\033[49m"


class Font:
    reset          = "\033[0m"
    bold           = "\033[1m"
    faint          = "\033[2m"
    italic         = "\033[3m"
    underline      = "\033[4m"
    slow_blink     = "\033[5m"
    rapid_blink    = "\033[6m"
    default        = "\033[99m"


class BackGround:
    black          = "\033[40m"
    red            = "\033[41m"
    green          = "\033[42m"
    yellow         = "\033[43m"
    blue           = "\033[44m"
    magenta        = "\033[45m"
    cyan           = "\033[46m"
    white          = "\033[47m"
    reset          = "\033[49m"


BG = BackGround()
FG = FontColor()
FONT = Font()

print(FG.__getattribute__("white))
