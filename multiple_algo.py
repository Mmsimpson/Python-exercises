def find_sum(multiples):
    sum = 0
    for i in range(multiples):
        if i % 3 == 0 or i % 5 == 0:
          sum += i 
    if multiples % 3 == 0 or multiples % 5 == 0:
      return sum 
print find_sum(1000)

