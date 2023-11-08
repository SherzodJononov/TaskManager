from helpers import *
from filecontorls import work

Users = User()
print()
print("1)Add User ")
print("2)Delete User ")
print("3)Check User ")
print("4)Shows User ")
print("5)Sign in User ")
print("6)Change Password ")
print()

while True:

    user_input = input("What do you do ? :-> ")

    if user_input == '1':
        try :
            # input Login and Password
            user_input_login = input("Enter the login : ")
            user_input_password = input("Enter the password : ")
            # Create file with name login
            Users.create_user(user_input_login,user_input_password)
            # Add password in file
                
        except :
            break

    elif user_input == '2':
        try :
            # input Login and Password
            user_input_login = input("Enter the login :")
            user_input_password = input("Enter the password :")
            # Create file with name login
            Users.delete_user(user_input_login,user_input_password)
            # Add password in file
            # break    
        except :
            break

    elif user_input == '3':

        try :
            # input Login and Password
            user_input_login = input("Enter the login : ")
            # user_input_password = input("Enter the password : ")
            # Create file with name login
            Users.check_user(user_input_login)
            # Add password in file
            # break    
        except :
            break
        
    elif user_input == '4':
        
        try:
            Users.show_users()
        except:
            print("User not found")

    elif user_input == '5' :

        try:
            user_input_login = input("Enter the login : ")
            user_input_password = input("Enter the password : ")
            Users.sign_in(user_input_login,user_input_password)
            work(user_input_login)
        except :
            print("Error Sign in User")    

    elif user_input == '6' :
        
        try:
            user_input_login = input("Enter the login : ")
            user_input_password = input("Enter the password : ")
            Users.change_password(user_input_login,user_input_password)
        except:
            print("Error Change Password")