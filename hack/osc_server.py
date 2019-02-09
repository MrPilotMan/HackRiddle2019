# Third party
from liblo import *

# Standard Lib
import time


class MuseServer(ServerThread):

    # Listen for messages on port 5002
    print("here")
    def __init__(self):
        ServerThread.__init__(self, 5001)


    # Receive accelrometer data
    @make_method('/muse/acc', 'fff')
    def acc_callback(self, path, args):
        acc_x, acc_y, acc_z = args
        print(f"{path} {acc_x} {acc_y} {acc_z}")


    # Receive EEG data
    @make_method('/muse/eeg', 'ffff')
    def eeg_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        print(f"{path} {l_ear} {l_forehead} {r_forehead} {r_ear}")


    # Handle unexpected messages
    @make_method(None, None)
    def fallback(self, path, args, types, src):
        print(f"Unknown message \
                \n\t Source: '{src.url}' \
                \n\t Address: '{path}' \
                \n\t Types: '{types} ' \
                \n\t Payload: '{args}'")

server = MuseServer()
server.start()
print(server.get_protocol())

if __name__ == "__main__":
    while 1:
        time.sleep(1)


