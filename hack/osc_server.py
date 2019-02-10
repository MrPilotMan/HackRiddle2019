# Local

# Third party
from liblo import *


def printer(thingy):
    print(thingy)


class MuseServer(ServerThread):
    data = 0

    # Listen for messages on port 5001
    def __init__(self):
        ServerThread.__init__(self, 5001)


    # Receive accelrometer data
    @make_method('/hack/elements/experimental/concentration', 'f')
    def concentration_callback(self, path, args):
        concentration = args
        print(concentration)
        data = concentration
        # print(f"{path} {concentration}")


    '''
    # Receive EEG data
    @make_method('/hack/eeg', 'ffff')
    def eeg_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        print(f"{path} {l_ear} {l_forehead} {r_forehead} {r_ear}")


    # Handle unexpected messages
    @make_method(None, None)
    def fallback(self, path, args, types, src):
        pass
    '''
