def sentence_maker(phrase):
    interrogotives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogotives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
print(sentence_maker("Hey how are you?"))


user_input = []
while True:
    
   
   
    convo = input("Say Something: ")
    
    
    
    if convo == '/end':
        break
    
     
   
        
    else:
        user_input.append(sentence_maker(convo))
        
print(" ".join(user_input))
    
        
    