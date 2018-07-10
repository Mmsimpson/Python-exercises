
sentence = "to be or not to be"

words= ['to', 'be', 'or', 'not', 'to', 'be']

word_count= {}
for word in words:
    if word in word_count:
          #to do
          word_count[word]= word_count[word] + 1 # or word_count[word] += 1
        else: 
            word_count[word]= 1
print word_count

#or

sentence= "to be or not to be"

padded_sentence= sentence + ' '

words= []

for char in padded_sentence:
    if char == ' ':
        words.append(curr_word)
        curr_word= ' '
        #todo
    else:
        curr_word += char 
words.append(curr_word)
print     