#list
my_list = ["e","d","c","x","z"]


#obtains user input
user_data = []
user_adding = input("Enter your data")
#my_list.append(user_adding)
user_option = input(f"select a to add {user_adding}\ne to extend to {user_adding}\np to delete {user_adding} from your list\nor select c to clear the list ")

#condition block that executes the users wishes
if user_option == "a":
    #append and extend are adding methods
    my_list.append(user_adding)
    print(my_list)
    
elif user_option == "e":
    
    new_list = my_list.extend([5, user_adding])
    print(f"Your list has been extended and {user_adding} has been added")
    print(new_list)
#pop and clear are removing methods  
elif user_option == "p":
    my_list.pop()
    print(f"{user_adding} has been removed from the list")
    print(my_list)
    
elif user_option == "c":
    new_list = my_list.clear()
    print("Your list has been cleared")
    print(new_list)
#error message telling user to enter a correct selection
else:
    print("You entered an incorrect selection please select a,e,p or c")
if user_adding in my_list:
    print(f"{user_adding} has been successfully added to your list.")
sort_list = input("Would you like to sort your list or reverse it?")
if sort_list =="sort":
    print(sorted(my_list))
elif sort_list == "reverse":
    my_list.reverse()
    print(my_list)
else:
    print(f"You did not choose to 'reverse' or to 'sort' here is your list:\n{my_list}")
    