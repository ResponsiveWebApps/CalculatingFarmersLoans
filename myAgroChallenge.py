# 1(a)
def get_days_of_power(R1, D1, R2, D2, R3, D3, K):

# By default Daily Rate(DR) and Days of Power(Pwr) are set to 0. There is no loan on the first day. 
  DR = 0
  Pwr = 0
  Day = 1
  Loan = False

  while K >= DR: 

# Activates the loans on their starting days.
    if D1 == Day:
      DR += R1
      Loan = True
    if D2 == Day:
      DR += R2
      Loan = True
    if D3 == Day:
      DR += R3
      Loan = True

# Takes daily rate from balance.
    K -= DR
    Day += 1

# Calculates days of power.   
    if Loan == True:
      Pwr += 1
  
  print("Total days of power: {}".format(Pwr))

# 1(b)
# Unit testing.
print("# Unit Testing")
get_days_of_power(3000, 3, 500, 10, 1500, 7, 700000)
get_days_of_power(500, 3, 500, 10, 500, 7, 21000)
get_days_of_power(1300, 0, 500, 0, 1500, 7, 10000)
get_days_of_power(10000, 3, 500, 10, 1500, 7, 11000)