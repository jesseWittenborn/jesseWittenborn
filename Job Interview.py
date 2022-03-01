#Jesse Wittenborn
#2/28/2022
#Job Interview



def main():

     
    
	name = input("what's your name?")
	question1 = input("Would you say you are intelligent?(Type y for yes and n for not intelligennt): ")
    
	
	     
	
	
	
	question2 = input("would you say you are a good problem solver? (Type y for yes and n for not a good problem solver): ")
    
	
	 
	
	question3 = input("Would you say you are tenacious? (Type y for yes and n for not tenacious): ")

	question4 = input("Do you work well with others? (Type y for yes and n for no): ")
	if(question1 == "y" and (question2 == "y" and (question3 == "y" and (question4 == "y" )))):
	  
		print("You are intelligent, and a hard worker. In addition, you are also tenacious, a good problem solver, and you work well with others. Expect a call from us soon "+name+"!")
	
	 
	     
	else:
	    print("Dont call us, we'll call you.")
	 
	 
	 

main()

