def calc_avg(muse_data):
    sum = 0
    for item in muse_data:
        sum += item
    avg = sum/len(muse_data)
    print(f"Average is {avg}")
