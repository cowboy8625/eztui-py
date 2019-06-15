from dataclasses import dataclass

@dataclass
class FontColor:
    red : str = '\033[31m'
    green : str = '\033[32m'
    yellow : str = '\033[33m'
    blue : str = '\033[34m'
    magenta : str = '\033[35m'
    cyan : str = '\033[36m'
    white : str = '\033[37m'
    bright_black : str = '\033[90m'
    bright_red : str = '\033[91m'
    bright_green : str = '\033[92m'
    bright_yellow : str = '\033[93m'
    bright_blue : str = '\033[94m'
    bright_magenta : str = '\033[95m'
    bright_cyan : str = '\033[96m'
    bright_white : str = '\033[97m'

@dataclass
class Font:
    reset : str = '\033[0m'
    bold : str = '\033[1m'
    faint : str = '\033[2m'
    italic : str = '\033[3m'
    underline : str = '\033[4m'
    slow_blink : str = '\033[5m'
    rapid_blink : str = '\033[6m'
    default : str = '\033[99m'

@dataclass
class BackGround:
    black : str= '\033[40m'
    red : str = '\033[41m'
    green : str = '\033[42m'
    yellow : str = '\033[43m'
    blue : str = '\033[44m'
    magenta : str = '\033[45m' 
    cyan : str = '\033[46m'
    white : str = '\033[47m'
    reset : str = '\033[49m'