# Third party
from liblo import *

class MuseServer(ServerThread):
    # Listen for messages on port 5001
    def __init__(self):
        ServerThread.__init__(self, 5001)
        self.data = [0]


    # Receive accelrometer data
    @make_method('/muse/elements/experimental/concentration', 'f')
    def concentration_callback(self, path, args):
        if args == 0 or args == 1:
            pass
        else:
            self.data = args


    '''
    # Receive EEG data
    @make_method('/muse/eeg', 'ffff')
    def eeg_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        print(f"{path} {l_ear} {l_forehead} {r_forehead} {r_ear}")

'''
    # Handle unexpected messages
    @make_method(None, None)
    def fallback(self, path, args, types, src):
        pass
