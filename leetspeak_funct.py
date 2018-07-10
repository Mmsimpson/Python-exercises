letters_to_convert['A', 'G', 'E', 'I', 'O', 'S', 'T']
numbers = [4, 3, 6 ,1, 0, 5, 7]
text = "hello marshall"
def convert(text):
    uppercased_text = text.upper()
    for letter in uppercased_text:
        print "the letter is ", letter
        counter = 0
        letter_to_add_to_translation = " "

