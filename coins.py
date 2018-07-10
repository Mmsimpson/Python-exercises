want_coins= 'y'
num_coins = 0 
print "You have %s coins." % num_coins
while want_coins !='N':
    want_coins = raw_input('Do you want another coin? (Y) (N)').upper()
    if want_coins == 'Y':
        num_coins = num_coins + 1
        print " You have %s coins." % num_coins
    elif want_coins == 'N':
        print "You have %s coins. bye!" % num_coins
    else:
        print "Invalid selection" 
    
