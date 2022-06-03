# PseudoCode Notes:

# Start at $100.00 and work backwards to $0.00
# Create a dictionary that defines what each denomiation of currency represents
# Use numbers for math and strings for reply message.
# Keep track of the number of times a bill or coin is added to total change due
# Make sure plural instances of denominations are accounted for



import itertools
# used later to merge lists 

def opitmal_change(item_cost, amount_paid):

    total_change = []
    num_of_bills_and_coins = []
    verbage = []
    num = 0
    currency = {
        10000: '$100',
        5000: '$50',
        2000: '$20',
        1000: '$10',
        500: '$5',
        100: '$1',
        25: '$.25',
        10: '$.10',
        5: '$.05',
        1: '$.01',
    }
    # dictionary of all possible change denominations

    total_due = round(amount_paid * 100 - item_cost * 100)
    # total change due in pennies (used to simplify decimal math)
    if total_due == 0:
        return(print("No Change Due"))
    elif total_due < 0:
        return(print("Insert More Cash To Recieve Item"))
    else:
     for change in currency:
        num = 0
        while int(total_due) >= int(change):
        # loop accesed so long as currency denomination can be subtracted from total change due
        # while loop utilizied to handle multiple occurences of the same denomination
            if num == 0:
            # this loop is accesed the first time a change denomination is required
                if total_due > 100:
                    total_change.append(currency[change])
                # included this if statement to not add coin values to final output
                num +=1
                total_due -= int(change)
                bill = "bill"
                quarter = "quarter"
                dime = "dime"
                nickel = "nickel"
                penny = "penny"
            else:
            # this loop accesed for multiple instances of the same change denomination
            # this loop also changes my verbage for plural situations
                num +=1
                total_due -= int(change)
                bill = "bills"
                quarter = "quarters"
                dime = "dimes"
                nickel = "nickels"
                penny = "pennies"
        if num > 0:
            # used to keep track of required number of each change denomation 
            num_of_bills_and_coins.append(str(num))
            # if/elif/else statements used to keep track of verbage variable
            if int(change) >= 100:
                verbage.append(str(bill))
            elif int(change) >= 25:
                verbage.append(str(quarter))
            elif int(change) >= 10:
                verbage.append(str(dime))
            elif int(change) >= 5:
                verbage.append(str(nickel))
            else:
                verbage.append(str(penny))
    
    # At this point there are three seperate sequential lists for:
    # 1: Number of each change denomiation
    # 2: Change type
    # 3: Change verbage
    # First the function prints the general return statement
    # Next, the three lits are merged together with itertools and printed to the screen. 

    print(f"The optimal change for an item that costs ${str(item_cost)} with an amount paid of ${str(amount_paid)} is: ")
    for (a, b, c) in itertools.zip_longest(num_of_bills_and_coins, total_change, verbage, fillvalue= ""):
        print(a , b, c)

