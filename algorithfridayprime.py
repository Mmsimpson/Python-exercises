number = 600851475143
remainder = number 
factor = 2
while remainder != 1:
    if remainder % factor == 0:
        remainder /= factor 
    else: 
        factor += 1

print factor





# done when the remainder = 1