#!/usr/bin/python

deposit = 100

apy = 5 / 100

years = 5

interest = deposit * apy
print("Interest:", interest)

earnings = interest + deposit

compound_interest = earnings * apy
print("Interest made after one year:", compound_interest)

compound_interest_final = compound_interest * years
print("Compound interest made after (x) years:", compound_interest_final + deposit)


