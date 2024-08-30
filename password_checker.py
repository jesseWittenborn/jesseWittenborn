
username=input('Enter your Username:')
password=input('Enter your Password:')




password_lenth = len(password)
hidden_password = '*' * password_lenth
shown_password = password

password_shower = input("Do you want to see your password")


print(f'{username}, your password, {hidden_password}, is {password_lenth} letters long')

if password_shower =="yes":
    print(shown_password)
