import time


def setup():
    start_time = time.time()
    return start_time


def calc_avg(muse_input):
    inputs = 0
    average = 0
    index = 1

    if index == 1:
        start_time = setup()


    now_time = time.time()
    inputs += muse_input
    average = inputs
    index += 1

    if (start_time - now_time) > 30:
        print(average)
        setup()

