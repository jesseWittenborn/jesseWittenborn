#Jesse Wittenborn
#10/12/2021-1/26/2022
#College Course Consultant

def cccgrades():
# Function that will find the average of the grades submitted	
	averageGrade = []
	
	
	for g in range(4):
		grades = int(input("What were your grades in 1 Math, 2 Reading and writing, 3 Communication, 4 Science: "))
		averageGrade.append(grades)
	ag = sum (averageGrade)/4
	print ( "Your grades were: ")
	
	print(averageGrade)
	
	if grades > 100:
		print (" Error please enter valid grades")
	averageGrade = grades/4
	if grades <= 100:
		print ( "Your average grade is: ")	
		print (ag)

def cccquiz():

# Quiz function to test user knowledge of subjects
	course = input("Welcome to College Course Consultant! Do you enjoy Math, reading and writing, Science, or Communication?")
	if (course == "math"):
		print("Excellent answer the next question correctly for your prospective majors")	
		question1 = float(input("What are the first 3 digits of pi?"))
	
	
	
		if question1 == 3.14:
			print("Your prospective majors are as follows: Fincance, Engineering, and Business")
		else:
			print("Incorrect Please try again or select a differant subject!")
	elif(course == "science"):
		print("Excellent answer the next question correctly for your prospective majors")
		question2 = input("Which science involves the study of the human body?") 
		if (question2 == "biology"):
			print("Your prospective majors are as follows: Medicine, Biology, Anatomy")
		else:
			print("Incorrect Please try again or select a differant subject!")
	elif(course == "reading and writing"):
		print("Excellent answer the next question correctly for your prospective majors")
		question3 = input("What is the name of the poetic device that gives human qualities or characteristics to something or someone that is not human?")
		if (question3 == "personification"):
			print("Your prospective majors are as follows: English, Journalism, Literature")
		else:
			print("Incorrect Please try again or select a differant subject!")
	elif(course == "communication"):
		print("Excellent answer the next question correctly for your prospective majors")
		question4 = input("What is the name of a communication technique often used in business to reach a mutually beneficial compromise?")
		if (question4 == "negotiation"):
			print("Your prospective majors are as follows: Business, Public Speaking, Project Management")
		else:
			print("Incorrect Please try again or select a differant subject!")
def main():

 
			 
# Welcoming message and User input of which skill they enjoy
    
	cccgrades()
	cccquiz()
	print("According to recent studies Business is the most common college major in America. Thank you for using College Course Consultant to plan for your future!")
main()
