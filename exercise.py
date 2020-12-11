import math

price = 1000000
good_credit = False

if good_credit:
    dwnpmt = 0.1 * price
else:
    dwnpmt = 0.2 * price

print(f" The downpayment is ${dwnpmt}")
