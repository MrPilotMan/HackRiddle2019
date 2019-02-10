from osc_server import MuseServer
from muse_math import calc_avg
import time as t

import time

if __name__ == "__main__":
    server = MuseServer()
    server.start()

    muse_data = []

    while True:
        print("1")
        time.sleep(1)

        muse_data.append(server.data)

        print(server.data)
        if len(muse_data) >= 300:
            calc_avg(muse_data)
            muse_data = []