import pathlib
import os
from hash_function import *

class User:
    
    line = pathlib.Path.cwd()

    def __init__(self) :
        pass
    
    def create_user(self,user_name,user_password):
        
        try:

            line = self.line / "USERS" / f"{user_name}"
            line.mkdir()
            line = self.line / "USERS" / f"{user_name}" / f"{user_name}_password.txt"
            line.touch()
            files = open(f"USERS.txt", "a")
            files.write(f"---{user_name}---\n")

            password_add = open(f"USERS\{user_name}\{user_name}_password.txt", "a")
            password_add.write(f"{Hash(user_password)}")
            
            line = self.line / "USERS" / f"{user_name}" / f"{user_name}_work.txt"
            line.touch()
            
        except:
            print("Error creating user")

    def check_user(self,user_name):

        try:

            line = self.line / "USERS" / f"{user_name}"

            if line.exists():
                print("You have this login")
            else:
                print("You don't have this login : ")

        except:
            print("Error checking user")

    def delete_user(self,user_name,user_password):
        files = open(f"USERS\{user_name}\{user_name}_password.txt" , "r")
        if Hash(user_password) == files.readline() :      
            
            self.delete_work(user_name)
                # line = self.line / "USERS" / f"{user_name}" / f"{user_name}_password.txt"   
                # line.unlink()
                # line = self.line / "USERS" / f"{user_name}" / f"{user_name}_work.txt"   
                # line.unlink()
                # line = self.line / "USERS" / f"{user_name}" 
                # line.rmdir() 
        
    def show_users(self):

        try:
            files = open("USERS.txt" , "r")
            print(files.read())
            files.close()
        except:
            print("Error show users")

    def sign_in(self, user_name,user_password):

        try:

            line = self.line / "USERS" / f"{user_name}"
            files = open(f"USERS\{user_name}\{user_name}_password.txt" , "r")
            if Hash(user_password) == files.readline() :
                line = self.line / "USERS"
                os.chdir(f"{line}")

            print(os.getcwd())

        except:
            print("Error sign in user")
    
    def change_password(self,user_name,user_password):
        try:
            line = self.line / "USERS" / f"{user_name}"
            files = open(f"USERS\{user_name}\{user_name}_password.txt" , "r")
            if Hash(user_password) == files.readline() :
                user_new_password = input("Enter new password : ")
            files = open(f"USERS\{user_name}\{user_name}_password.txt" , "w")
            files.write(f"{Hash(user_new_password)}")
            files.close()
        except:
            print("Error changing password")

    
    def count_user(self,user_name):
        k = 0
        files = open("USERS.txt", "r")
        files.read()
        for index,value in enumerate(files):
            if value == user_name:
                k = index
        return k

    def delete_from_users(self,user_name):
        files = open("USERS.txt", "r")
        lines = files.readlines()
        files = open("USERS.txt", "w")
        for index,line in enumerate(lines):
            
            if index == self.count_user(user_name):
                continue
            else :
                files.write(line)

    def delete_password(self,user_name):
        line = self.line / "USERS" / f"{user_name}" / f"{user_name}_password.txt"
        line.unlink()

    def delete_work(self,user_name):
        line = self.line / "USERS" / f"{user_name}" / f"{user_name}_work.txt"
        line.unlink()
    