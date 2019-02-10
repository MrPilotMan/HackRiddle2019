from asciimatics.screen import Screen
import time

def demo(screen, passed_value):

    screen.print_at('''
    ___.           __
    ''', 0, 0)
    screen.print_at('''
    \_ |__   _____/  |______    _____ _____  ___  ___
    ''', 0, 1)
    screen.print_at('''
    | __ \_/ __ \   __\__  \  /     \\__  \ \  \/  /
    ''', 0, 2)

    screen.print_at('''
    | \_\ \  ___/|  |  / __ \|  Y Y  \/ __ \_>    <
    ''', 0, 3)

    screen.print_at('''
    |___  /\___  >__| (____  /__|_|  (____  /__/\_ \
    ''', 0, 4)

    screen.print_at('''
        \/     \/          \/      \/     \/      \/
    ''', 0, 5)

    screen.print_at(str(passed_value[0]), 0, 6)
    screen.print_at(str(passed_value[1]), 0, 7)
    screen.print_at(str(passed_value[2]), 0, 8)

    screen.refresh()
    time.sleep(.3)
