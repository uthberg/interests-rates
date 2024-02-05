#!/usr/bin/python

deposit = 100 #initial starting value 

apy = 5 / 100 #5.00 convert percent annual percentage yield into a decimal

years = 5 #over 5 year time frame

interest = deposit * apy
print("Interest:", interest)

earnings = interest + deposit

compound_interest = earnings * apy
print("Interest made after one year:", compound_interest)

compound_interest_final = compound_interest * years
print("Compound interest made after 5 years:", compound_interest_final + deposit)


