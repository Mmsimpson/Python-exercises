word= raw_input('Please enter a word: ')
diction={}
for char in word:
    #for every letter in word- increase letter value by 1.
    diction[char]= 1 
    #if letter already in dict: 
    if char in diction:
        diction[char] += 1
    else: diction[char]= 1
        
    