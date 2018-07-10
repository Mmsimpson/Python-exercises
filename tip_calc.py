bill = raw_input ("Total bill amount? ")
bill= float(bill)

print bill
service = raw_input("Level of service? ")

 
if service == "good":
    tip_amount= bill * .20
elif service == "fair":
    tip_amount= bill * .15
elif service == "bad":
    tip_amount= bill * .10

print "$%.2f" % tip_amount

total_amount= bill + tip_amount
print "$%.2f"  % total_amount



