# Third party
from liblo import *

# Standard Lib
import time


def printer(thingy):
    print(thingy)

class MuseServer(ServerThread):

    # Listen for messages on port 5001
    def __init__(self):
        ServerThread.__init__(self, 5001)


    # Receive accelrometer data
    @make_method('/muse/elements/experimental/concentration', 'f')
    def concentration_callback(self, path, args):
        concentration = args
        printer(concentration)
        #print(f"{path} {concentration}")


    # Receive EEG data
    #@make_method('/muse/eeg', 'ffff')
    #def eeg_callback(self, path, args):
    #    l_ear, l_forehead, r_forehead, r_ear = args
    #    print(f"{path} {l_ear} {l_forehead} {r_forehead} {r_ear}")


    # Handle unexpected messages
    @make_method(None, None)
    def fallback(self, path, args, types, src):
        pass

server = MuseServer()
server.start()
#print(server.get_protocol())

if __name__ == "__main__":
    while 1:
        time.sleep(1)