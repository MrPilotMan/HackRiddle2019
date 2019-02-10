from osc_server import MuseServer
from muse_math import calc_avg
import time as t
import datetime

delay = 30

if __name__ == "__main__":
    server = MuseServer()
    server.start()
    print("server started")
    endTime = t.time() + delay

    muse_data = []

    while True:
        #t.sleep(.1)

        #print(server.data[0])
        muse_data.append(server.data[0])


        if t.time() >= endTime:
            print(datetime.datetime.now().time(), " -- Average: ", (sum(muse_data) / len(muse_data)))
            endTime = t.time() + delay
            #print(muse_data)
            #calc_avg(muse_data)
            muse_data = []
