#!/usr/bin/python

deposit = 100 
apy = 5 / 100
years = 10

# Calculate the interest and earnings after one year
interest = deposit * apy
earnings = interest + deposit

# Calculate compound interest for the given number of years
compound_interest = deposit * ((1 + apy) ** years) - deposit

print("Interest:", interest)
print("Earnings after one year:", earnings)
print("Compound interest earnings after", years, "years:", compound_interest + deposit)
