#input that requests the user's Username and password
username=input('Enter your Username:')
password=input('Enter your Password:')



#Checks password length
password_lenth = len(password)
#Prints '*' the length of the password to hide the password
hidden_password = '*' * password_lenth
#Variable that equals the user's password
shown_password = password
#Input asking the user if he would like to display his password
password_shower = input("Do you want to see your password")

#Prints the password legnth and hides it using '*'
print(f'{username}, your password, {hidden_password}, is {password_lenth} letters long')
#If the user chooses to see the password the password is displayed with this conditional
if password_shower =="yes":
    print(shown_password)
