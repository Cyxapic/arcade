from .miniature import Miniature
from .messages import Message
from .button import Button
from .commands import GameStartMouseCmd, GoMenuCmd, LeaveGameCmd


miniature = Miniature
message = Message
button = Button

game_start_mouse_cmd = GameStartMouseCmd('gen_lvl')
go_menu_cmd = GoMenuCmd('menu')
leave_game_cmd = LeaveGameCmd('menu')
