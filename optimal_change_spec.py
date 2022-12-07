# Write your tests here!
from improved_vending_machine import optimal_change

# The first varriable is the cost of the item, the second variable is the payment received

print(optimal_change(100.00, 50.00))
# expected output:
# Insert More Cash To Recieve Item

print(optimal_change(100.00, 100.00))
# expected output:
# No Change Due

print(optimal_change(50.00, 100.00))
# expected output:
# The optimal change for an item that costs 50.0 with an amount paid of 100.0 is:
# 1 $50 bill

print(optimal_change(99.99, 100.00))
# expected output:
# The optimal change for an item that costs 99.99 with an amount paid of 100.0 is:
# 1  penny

print(optimal_change(1.00, 100.00))
# expected output:
# The optimal change for an item that costs 1.0 with an amount paid of 100.0 is:
# 1 $50 bill
# 2 $20 bills
# 1 $5 bill
# 4 $1 bills

print(optimal_change(.01, 100.00))
# expected output:
# The optimal change for an item that costs 0.01 with an amount paid of 100.0 is:
# 1 $50 bill
# 2 $20 bills
# 1 $5 bill
# 4 $1 bills
# 3  quarters
# 2  dimes
# 4  pennies

print(optimal_change(0.01, 0.92))
# output:
# The optimal change for an item that costs $0.01 with an amount paid of $0.92 is:
# 3 quarters
# 1 dime
# 1 nickel
# 1 penny
