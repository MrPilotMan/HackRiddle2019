from osc_server import MuseServer
from muse_math import *
import time as t
import datetime
import csv

delay = 10

if __name__ == "__main__":
    server = MuseServer()
    server.start()
    endTime = t.time() + delay
    print("server started")

    input = open('user_data.csv', 'r')


    # Lists of data points gathered from Muse headset
    alpha_data = []
    beta_data = []
    theta_data = []

    alpha_low = 1
    alpha_high = 0
    beta_low = 1
    beta_high = 0
    theta_low = 1
    theta_high = 0

    #grab the user data
    with input:
        reader = csv.reader(input)
        for row in reader:
            row_num = 0
            col_num = 0
            for value in row:
                if row_num == 0:
                    if col_num == 1:
                        alpha_low = float(value)
                    if col_num == 2:
                        alpha_high = float(value)
                if row_num == 1:
                    if col_num == 1:
                        beta_low = float(value)
                    if col_num == 2:
                        beta_high = float(value)
                if row_num == 2:
                    if col_num == 1:
                        theta_low = float(value)
                    if col_num == 2:
                        theta_high = float(value)
                col_num += 1
            row_num += 1

    while True:
        if server.connection is True:

            alpha_data.append(server.alpha_data)
            beta_data.append(server.beta_data)
            theta_data.append(server.theta_data)

            if t.time() >= endTime and len(alpha_data) > 1:

                def up_csv():
                    csv_data = [
                    ["alpha", alpha_low, alpha_high],
                    ["beta", beta_low, beta_high],
                    ["theta", theta_low, theta_high],
                    ]

                    print(csv_data)

                    output = open('user_data.csv', 'w')

                    with output:

                        writer = csv.writer(output)

                        for row in csv_data:
                            writer.writerow(row)

                #calculate averages
                alpha_avg = sum(alpha_data) / len(alpha_data)
                beta_avg = sum(beta_data) / len(beta_data)
                theta_avg = sum(theta_data) / len(theta_data)

                if alpha_avg < alpha_low:
                    alpha_low = alpha_avg
                    up_csv()

                if alpha_avg > alpha_high:
                    alpha_high = alpha_avg
                    up_csv()

                if beta_avg < beta_low:
                    beta_low = beta_avg
                    up_csv()

                if beta_avg > beta_high:
                    beta_high = beta_avg
                    up_csv()

                if theta_avg < theta_low:
                    theta_low = theta_avg
                    up_csv()

                if theta_avg > theta_high:
                    theta_high = theta_avg
                    up_csv()


                print(f'''alpha: {alpha_avg} \nbeta: {beta_avg} \ntheta: {theta_avg}''')

                #statistical_analysis(alpha_avg, beta_avg, theta_avg)

                '''
                alpha_individual_score = individual_score("alpha", alpha_average)
                beta_individual_score = individual_score("beta", alpha_average)
                theta_individual_score = individual_score("theta", alpha_average)
                '''

                alpha_data.clear()
                beta_data.clear()
                theta_data.clear()

                #print(datetime.datetime.now().time(), " -- Average: ", (sum(muse_data) / len(muse_data)))
                endTime = t.time() + delay
        else:
            print("Bad Connection")
            t.sleep(1)
