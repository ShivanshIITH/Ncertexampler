import random

desired_products = [6, 7, 12]
total_trials = 1000000  # answers are varying slightly due to the probabilistic nature of the simulation, so i increase the number of trials to get closer to  desired probabilities. 

count_6 = 0
count_7 = 0
count_12 = 0

i = 0
while i < total_trials:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    product = die1 * die2
    
    if product == 6:
        count_6 += 1
    elif product == 7:
        count_7 += 1
    elif product == 12:
        count_12 += 1
    
    i += 1

probability_6 = count_6 / total_trials
probability_7 = count_7 / total_trials
probability_12 = count_12 / total_trials

print(f"Probability of product 6: {probability_6:.3f}")
print(f"Probability of product 7: {probability_7:.3f}")
print(f"Probability of product 12: {probability_12:.3f}")
