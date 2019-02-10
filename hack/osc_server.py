from liblo import *

class MuseServer(ServerThread):
    '''
    Alpha corresponds to relaxed
    Beta corresponds to active thinking
    Theta corresponds to drowsiness
    '''
    # Listen for messages on port 5001
    def __init__(self):
        ServerThread.__init__(self, 5001)
        self.alpha_data = 0
        self.beta_data = 0
        self.theta_data = 0
        self.connection = False

    # Receive alpha
    @make_method('/muse/elements/alpha_absolute', 'ffff')
    def alpha_callback(self, path, args):
        if self.connection == True:
            #print(f"alpha: {args}")
            self.alpha_data = sum(args)/4

    # Receive beta
    @make_method('/muse/elements/beta_absolute', 'ffff')
    def beta_callback(self, path, args):
        if self.connection == True:
            #print(f"beta: {args}")
            self.beta_data = sum(args)/4

    # Receive theta
    @make_method('/muse/elements/theta_absolute', 'ffff')
    def theta_callback(self, path, args):
        if self.connection == True:
            #print(f"theta: {args}")
            self.theta_data = sum(args)/4


    @make_method('/muse/elements/horseshoe', 'ffff')
    def horseshoe_callback(self, path, args):
        if sum(args) == 4:
            self.connection = True


    '''
    # Receive EEG data
    @make_method('/muse/eeg', 'ffff')
    def eeg_callback(self, path, args):
        l_ear, l_forehead, r_forehead, r_ear = args
        print(f"{path} {l_ear} {l_forehead} {r_forehead} {r_ear}")



    # Handle unexpected messages
    @make_method(None, None)
    def fallback(self, path, args, types, src):
        print(path)

    '''
