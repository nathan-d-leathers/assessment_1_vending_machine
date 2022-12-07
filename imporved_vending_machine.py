# -=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-==-=-=-=-=-=-=-=-
# Assessment #1:

# Create a vending machine that returns correct change for items up to $100

# -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import itertools

def opitmal_change(item_cost, amount_paid):
    total_change = []
    num_of_bills_and_coins = []
    verbage = []
    answer = []
    
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

    total_due = round(amount_paid * 100 - item_cost * 100)
    if total_due == 0:
        return("No Change Due")
    elif total_due < 0:
        return("Insert More Cash To Recieve Item")
    else:
     for change in currency:
        num = 0
        while int(total_due) >= int(change):
            if num == 0:
                if total_due > 100:
                    total_change.append(currency[change])
                num +=1
                total_due -= int(change)
                bill = "bill"
                quarter = "quarter"
                dime = "dime"
                nickel = "nickel"
                penny = "penny"
            else:
                num +=1
                total_due -= int(change)
                bill = "bills"
                quarter = "quarters"
                dime = "dimes"
                nickel = "nickels"
                penny = "pennies"
        if num > 0:
            num_of_bills_and_coins.append(str(num))
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
                
    price = item_cost    
    payment = amount_paid
    optimal_statement = "The optimal change for an item that costs $" + str(f"{price:.2f} ") + "with an amount paid of $" + str(f"{payment:.2f} ") + "is "
    a_tracker = 0

    for (a, b, c) in itertools.zip_longest(num_of_bills_and_coins,total_change, verbage, fillvalue= ""):
        if a_tracker == len(num_of_bills_and_coins) -1:
            answer.append("and " + a)
        else:
            answer.append(a)
            a_tracker += 1
        if b != "":
            answer.append(b)
        answer.append(c + ",")
    answer[-1] = c + "."
    change_due = " ".join(answer)
    return(optimal_statement + change_due)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-

# All Bugs Fixed!!!

# -=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-==-=-=-=-=-=-=--=-=-=-=-=-=-