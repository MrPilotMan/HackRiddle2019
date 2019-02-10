
alpha_averages = []
beta_averages = []
theta_averages = []

def calc_avg(to_be_averaged):
    print(datetime.datetime.now().time(), " -- Average: ", (sum(to_be_averaged) / len(to_be_averaged)))


def concentration_score(alpha, beta, theta, alpha_low, alpha_high, beta_low, beta_high, theta_low, theta_high):

    alpha_averages.append(alpha)
    beta_averages.append(beta)
    theta_averages.append(theta)

    # Resize lists to only 5 items
    if len(alpha_averages) > 5:
        alpha_averages.pop(0)

    if len(beta_averages) > 5:
        beta_averages.pop(0)

    if len(theta_averages) > 5:
        theta_averages.pop(0)

    if len(alpha_averages) == 5:

        alpha_trailing = sum(alpha_averages) / 5
        beta_trailing = sum(beta_averages) / 5
        theta_trailing = sum(theta_averages) / 5

        if alpha_trailing <= (alpha_high - alpha_low):
            alpha_score = 0
        else:
            alpha_score = 1

        if beta_trailing <= (beta_high - beta_low):
            beta_score = 0
        else:
            beta_score = 1

        if theta_trailing <= (theta_high - theta_low):
            theta_score = 0
        else:
            theta_score = 1


        #[on_true] if [expression] else [on_false]
        "HIGH" if [alpha_score] else "LOW"
        "HIGH" if [beta_score] else "LOW"
        "HIGH" if [theta_score] else "LOW"

        '''
        alpha_string = ("HIGH", "LOW")[alpha_score]
        beta_string = ("HIGH", "LOW")[beta_score]
        theta_string = ("HIGH", "LOW")[theta_score]
        '''


        print("Scores: ", datetime.datetime.now().time(), f":\nAlpha: {alpha_string}\nBeta: {beta_score}\nTheta: {theta_score}")
