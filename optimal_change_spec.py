# Write your tests here!
from optimal_change import opitmal_change


opitmal_change(100.00, 50.00)
# expected output:
# Insert More Cash To Recieve Item

opitmal_change(100.00,100.00)
# expected output:
# No Change Due

opitmal_change(50.00,100.00)
# expected output:
# The optimal change for an item that costs 50.0 with an amount paid of 100.0 is: 
# 1 $50 bill

opitmal_change(99.99,100.00)
# expected output:
# The optimal change for an item that costs 99.99 with an amount paid of 100.0 is: 
# 1  penny

opitmal_change(1.00,100.00)
# expected output:
# The optimal change for an item that costs 1.0 with an amount paid of 100.0 is: 
# 1 $50 bill
# 2 $20 bills
# 1 $5 bill
# 4 $1 bills

opitmal_change(.01,100.00)
# expected output:
# The optimal change for an item that costs 0.01 with an amount paid of 100.0 is: 
# 1 $50 bill
# 2 $20 bills
# 1 $5 bill
# 4 $1 bills
# 3  quarters
# 2  dimes
# 4  pennies

