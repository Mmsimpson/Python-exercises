tip= raw_input("How muh do you want to tip?")
float(tip) * 2.0

import math

#example Code
tip = raw_input("Be honest, hiw much did you tip?")
tip= float(tip_input)

bill_inout = raw_input("How much was the bill?")
bill= float(bill_input)


tip_ratio = tip / bill

if tip_ratio < 0.10:
    print "Stingy!"
    
elif tip_ratio > 0.20:
    say "generous!"

else:
    print "average!"
