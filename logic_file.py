# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-
#          THIS FILE IS IS MY SCRATCH PAPER I USED TO FIGURE OUT THE LOGIC OF THE PROBLEM
#          IT DOES NOT INTERACT WITH MY CODE IN ANY WAY THAT AFFECTS THE ASSIGNMENT
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-


# Notes:
# Should Start at $100.00 and work backwards to $0.00
# Should have a dictionary that defines what each denomiation of currency repsresents
# Should make sure we are using numbers for math and strings for replies.
# Should interpolate an 's' on the end of denominations that are duplicates. interpolate it in.
# Penny has to change to Pennies 


# def opitmal_change(item_cost, amount_paid):

#     total_due = amount_paid - item_cost
#     if total_due == 0:
#         print("No Change Due")
#     elif total_due < 0:
#         print("Insert More Cash To Recieve Item")
#     else:
#         print("this is a test of the emergency vending system")
  
# timothy = opitmal_change(25.00, 45.00)
# larry = opitmal_change(25.00, 25.00)
# barry = opitmal_change(25.00, 5.00)
# if/elif/else outputs correct statements
# this is a test of the emergency vending system
# No Change Due
# Insert More Cash To Recieve Item
# -=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# item_cost = 45.01
# amount_paid = 80.02
     
# total_due = round(amount_paid * 100 - item_cost * 100)
# print(total_due)
# prints out floats of .000000000001, but we should be able to truncate it with round()

# item_cost = 0.09
# amount_paid = 100
# total_due = round(amount_paid * 100 - item_cost * 100)
# print(total_due)
# outputs correct logically value

# -=-=-=-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=--=-=-


# def opitmal_change(item_cost, amount_paid):
#     total_change = []
#     num = 1
#     currency = {
#         100: 10000,
#         50: 5000,
#         20: 2000,
#         10: 1000,
#         5: 500,
#         1: 100,
#         .25: 25,
#         .10: 10,
#         .05: 5,
#         .01: 1,
#     }

#     total_due = round(amount_paid * 100 - item_cost * 100)

#     for change in currency:
#         if int(total_due) >= int(change):
#             total_change.append(currency[change])
#             total_due -= int(change)
#             num +=1
#     return total_change

# timothy = opitmal_change(20.00, 100.00)
# print(timothy)
# # output: correct list but as values and not keys.

# # -=-=-=-
# def opitmal_change(item_cost, amount_paid):
#     total_change = []
#     num = 1
#     currency = {
#         100: 10000,
#         50: 5000,
#         20: 2000,
#         10: 1000,
#         5: 500,
#         1: 100,
#         .25: 25,
#         .10: 10,
#         .05: 5,
#         .01: 1,
#     }

#     total_due = round(amount_paid * 100 - item_cost * 100)

#     for change in currency:
#         if total_due >= currency[change]:
#             total_change.append(currency[change])
#             total_due -= currency[change]
#             num +=1
#     return total_change

# timothy = opitmal_change(20.00, 100.00)
# print(timothy)
# -==--=-=-

# -==-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=--=-=--=--=-=-=-=-=-==-=-=-
# Logic Flows Correctly!
# def opitmal_change(item_cost, amount_paid):
#     total_change = []
#     num = 1
#     currency = {
#         10000: '$100',
#         5000: '$50',
#         2000: '$20',
#         1000: '$10',
#         500: '$5',
#         100: '$1',
#         25: 'Quarter',
#         10: 'Dime,',
#         5: 'Nickel',
#         1: 'Penny'
#     }

#     total_due = round(amount_paid * 100 - item_cost * 100)
  
#     for change in currency:
#         while int(total_due) >= int(change):
#             total_change.append(currency[change])
#             total_due -= int(change)
#             num +=1
#     return total_change

# timothy = opitmal_change(15.78, 100.00)
# print(timothy)
# correct change is $84.22
# output: ['$50', '$20', '$10', '$1', '$1', '$1', '$1', 'Dime,', 'Dime,', 'Penny', 'Penny']

# -=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-==-=-=-=-=--=--

# def opitmal_change(item_cost, amount_paid):
#     total_change = []
#     num = 1
#     currency = {
#         10000: '$100',
#         5000: '$50',
#         2000: '$20',
#         1000: '$10',
#         500: '$5',
#         100: '$1',
#         25: 'Quarter',
#         10: 'Dime,',
#         5: 'Nickel',
#         1: 'Penny'
#     }

#     total_due = round(amount_paid * 100 - item_cost * 100)
  
#     for change in currency:
#         while int(total_due) >= int(change):
#             total_change.append(currency[change])
#             total_due -= int(change)
#             num +=1

#     print(f"The optimal change for an item that costs {item_cost} with an amount paid of {amount_paid} is ...insert here...")

# timothy = opitmal_change(15.78, 100.00)
# print(timothy)
# correct change is $84.22
# output: ['$50', '$20', '$10', '$1', '$1', '$1', '$1', 'Dime,', 'Dime,', 'Penny', 'Penny']
# example of desired output format: "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."
# The optimal change for an item that costs 15.78 with an amount paid of 100.0 is ...insert here...

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# def opitmal_change(item_cost, amount_paid):
    
#     num_of_bills_and_coins = []
#     total_change = []
#     verbage = []
    
#     num = 0
#     currency = {
#         10000: '$100',
#         5000: '$50',
#         2000: '$20',
#         1000: '$10',
#         500: '$5',
#         100: '$1',
#         25: '$.25',
#         10: '$.10',
#         5: '$.05',
#         1: '$.01',
#     }

#     total_due = round(amount_paid * 100 - item_cost * 100)
  
#     for change in currency:
#         num = 0
#         while int(total_due) >= int(change):
#             if num == 0:
#                 total_change.append(currency[change])
#                 num +=1
#                 total_due -= int(change)
#                 bill = "bill"
#                 quarter = "quarter"
#                 dime = "dime"
#                 nickel = "nickel"
#                 penny = "penny"
#             else:
#                 num +=1
#                 total_due -= int(change)
#                 bill = "bills"
#                 quarter = "quarters"
#                 dime = "dimes"
#                 nickel = "nickels"
#                 penny = "pennies"
#         if num > 0:
#             num_of_bills_and_coins.append(str(num))
#             if int(change) >= 100:
#                 verbage.append(str(bill))
#             elif int(change) >= 25:
#                 verbage.append(str(quarter))
#             elif int(change) >= 10:
#                 verbage.append(str(dime))
#             elif int(change) >= 5:
#                 verbage.append(str(nickel))
#             else:
#                 verbage.append(str(penny))

#     print(num_of_bills_and_coins)           
#     print(total_change)
#     print(verbage)    
          
   
#     return_statement = f"The optimal change for an item that costs {item_cost} with an amount paid of {amount_paid} is "
   
# timothy = opitmal_change(15.78, 100.00)
# print(timothy)
# output:
# ['1', '1', '1', '4', '2', '2']
# ['$50', '$20', '$10', '$1', '$.10', '$.01']
# ['bill', 'bill', 'bill', 'bills', 'dimes', 'pennies']

# -=-=-=-=-=-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=
# import itertools
# def opitmal_change(item_cost, amount_paid):
    
#     num_of_bills_and_coins = []
#     total_change = []
#     verbage = []
    
#     num = 0
#     currency = {
#         10000: '$100',
#         5000: '$50',
#         2000: '$20',
#         1000: '$10',
#         500: '$5',
#         100: '$1',
#         25: '$.25',
#         10: '$.10',
#         5: '$.05',
#         1: '$.01',
#     }

#     total_due = round(amount_paid * 100 - item_cost * 100)
  
#     for change in currency:
#         num = 0
#         while int(total_due) >= int(change):
#             if num == 0:
#                 total_change.append(currency[change])
#                 num +=1
#                 total_due -= int(change)
#                 bill = "bill"
#                 quarter = "quarter"
#                 dime = "dime"
#                 nickel = "nickel"
#                 penny = "penny"
#             else:
#                 num +=1
#                 total_due -= int(change)
#                 bill = "bills"
#                 quarter = "quarters"
#                 dime = "dimes"
#                 nickel = "nickels"
#                 penny = "pennies"
#         if num > 0:
#             num_of_bills_and_coins.append(str(num))
#             if int(change) >= 100:
#                 verbage.append(str(bill))
#             elif int(change) >= 25:
#                 verbage.append(str(quarter))
#             elif int(change) >= 10:
#                 verbage.append(str(dime))
#             elif int(change) >= 5:
#                 verbage.append(str(nickel))
#             else:
#                 verbage.append(str(penny))
    
#     print(f"The optimal change for an item that costs {str(item_cost)} with an amount paid of {str(amount_paid)} is: ")
#     for (a, b, c) in itertools.zip_longest(num_of_bills_and_coins, total_change, verbage, fillvalue=""):
#         print(a + "x", b, c)
  
    
# timothy = opitmal_change(15.78, 100.00)
# The optimal change for an item that costs 15.78 with an amount paid of 100.0 is: 
# 1x $50 bill
# 1x $20 bill
# 1x $10 bill
# 4x $1 bills
# 2x $.10 dimes
# 2x $.01 pennies

# -=-=-=-=-=--==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# import itertools
# def opitmal_change(item_cost, amount_paid):
#     total_change = []
#     num_of_bills_and_coins = []
#     verbage = []
    
#     num = 0
#     currency = {
#         10000: '$100',
#         5000: '$50',
#         2000: '$20',
#         1000: '$10',
#         500: '$5',
#         100: '$1',
#         25: '$.25',
#         10: '$.10',
#         5: '$.05',
#         1: '$.01',
#     }

#     total_due = round(amount_paid * 100 - item_cost * 100)
#     if total_due == 0:
#         return(print("No Change Due"))
#     elif total_due < 0:
#         return(print("Insert More Money To Recieve Item"))
#     else:
#         for change in currency:
#             num = 0
#             while int(total_due) >= int(change):
#                 if num == 0:
#                     if total_due > 100:
#                         total_change.append(currency[change])
#                     num +=1
#                     total_due -= int(change)
#                     bill = "bill"
#                     quarter = "quarter"
#                     dime = "dime"
#                     nickel = "nickel"
#                     penny = "penny"
#                 else:
#                     num +=1
#                     total_due -= int(change)
#                     bill = "bills"
#                     quarter = "quarters"
#                     dime = "dimes"
#                     nickel = "nickels"
#                     penny = "pennies"
#             if num > 0:
#                 num_of_bills_and_coins.append(str(num))
#                 if int(change) >= 100:
#                     verbage.append(str(bill))
#                 elif int(change) >= 25:
#                     verbage.append(str(quarter))
#                 elif int(change) >= 10:
#                     verbage.append(str(dime))
#                 elif int(change) >= 5:
#                     verbage.append(str(nickel))
#                 else:
#                     verbage.append(str(penny))
                
#         print(f"The optimal change for an item that costs {str(item_cost)} with an amount paid of {str(amount_paid)} is: ")
#         for (a, b, c) in itertools.zip_longest(num_of_bills_and_coins, total_change, verbage, fillvalue= ""):
#             print(a , b, c)      
   
    
# timothy = opitmal_change(100.00, 10.00)
# # output:
# The optimal change for an item that costs 15.78 with an amount paid of 100.0 is: 
# 1 $50 bill
# 1 $20 bill
# 1 $10 bill
# 4 $1 bills
# 2  dimes
# 2  pennies




# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-
#           NOTES FOR FUTURE IMPROVEMENTS:
#   -Figure out how to keep .00 format on return string
#   -figure out how to append using itertools.zip, or how to push into a string
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-
