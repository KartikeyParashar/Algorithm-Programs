# Write a Util Static Function to calculate monthlyPayment that reads in three
# command­line arguments P, Y, and R and calculates the monthly payments you
# would have to make over Y years to pay off a P principal loan amount at R per cent
# interest compounded monthly. The formula is The formula is
#
#                 P*r
# payment = ----------------- , n=12*Y , r = R/(12*100)
#            1 - (1+r)**(-n)

def monthly_payment(principle,year,interest):
    n = (12*year)
    r = interest/(12*100)
    return (principle*r)/(1 - pow(1+r,-n))

payment = monthly_payment(50000,5,10)
print(f"The monthly payment you have to make is {round(payment,2)} rupees")
