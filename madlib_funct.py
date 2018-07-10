#print "Please fill in the blanks below:"
#print "____(name)____'s favorite subject in school is ____(subject)____."

#... madlib(message): 
    print "Please fill in the blanks below:"      
    print "____(name)____'s favorite subject in school is ____(subject)____."
    template = "%s's favorite subject in school is %s" % (name, subject) 
    message  = template
    for name in template:
        name = raw_input("What is name ?")
    for subject in template:
        subject = raw_input("What is subject ")  
   #return message...
marshall = {'class' : 'chemistry', 'hobby' : 'cooking', }
def store_responses():
    print "Please fill in the blanks below:"      
    print "____(name)____'s favorite subject in school is ____(subject)____."

