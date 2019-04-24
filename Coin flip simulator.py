# Coin flip simulator
# Apps is doing con flips and counts total of heads and tails

import random

tails = 0
heads = 0
total = 0


while total < 100:
    coin = random.randint(1,2)
    if coin == 1:
        heads += 1
    else:
        tails += 1
    total += 1

print("Amount of heads is:", heads, "and tails is:", tails)
print("Total", total, " flips.")

input("\n\nEnter")
