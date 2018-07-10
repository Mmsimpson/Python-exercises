input= int(raw_input('How big is the square?'))
square = '*' * input 
rows = 0 
while rows < input:
    print (square)
    rows = rows + 1

######
#Use a for loop
input= int(raw_input('How big is the square?'))
square= '*' input 
for i in range(0, input):
