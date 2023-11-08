import pathlib
import os

class filecontrols:

    line = pathlib.Path.cwd()

    def __init__(self,file_name):
        self.file_name = file_name

    def add_work(self):

        try:
            
            # line = self.line / f"{self.file_name}.txt"
            files = open(f"{self.file_name}\{self.file_name}_work.txt", "a")
            title = input("Enter a title :")
            description = input("Enter a description :")
            priority = input("Enter a priority :")
            due_date = input("Enter a date :")
            status = input("Enter a status :") 
            self.task = f"title :{title}| description :{description}| priority :{priority}| due_date :{due_date} | status :{status}\n" 
            files.write(f"{self.task}")
     
        except:
            print("Try again")

    def delete_work(self,work):

        try:
            self.delete_from_users(work)
        except:
            print("Error deleting")

    def change_work(self,work):
       
        try:
       
            counter = self.count_user(work)
            files = open(f"{self.file_name}\{self.file_name}_work.txt", "r")
            lines = files.readlines()
            files = open(f"{self.file_name}\{self.file_name}_work.txt", "w")

            for index,line in enumerate(lines):
                if index == counter :
                    x = line
                    break

            self.delete_from_users(work)
            title = input("Enter a title :")
            description = input("Enter a description :")
            priority = input("Enter a priority :")
            due_date = input("Enter a date :")
            status = input("Enter a status :") 
            task = f"title :{title}| description :{description}| priority :{priority}| due_date :{due_date} | status :{status}\n" 
            files.write(task)
            files.close()
      
        except:
            print("Try again")

    def get_work(self):
        try:
            print()
            print("1)Complete")
            print("2)Not Complete")
            print("3)Our task")
            print()
            user_input = input("Whick task you want to see ? :")
            if user_input == "1" :
                self.get_completed_notcomplet_work("complete")
        
            elif user_input == "2" :
                self.get_completed_notcomplet_work("not complete")
        
            elif user_input == '3':
                try:
                
                    files = open(f"{self.file_name}\{self.file_name}_work.txt", "r")
                    lines = files.readlines()
                    files = open(f"{self.file_name}\{self.file_name}_work.txt", "r")
                    for index,line in enumerate(lines):
                            print(line)

                except:
                    print("Try again")
        except:
            print("Try again")
    def count_user(self,work):
        
        try:
      
            k = 0
            files = open(f"{self.file_name}\{self.file_name}_work.txt", "r")
            x = files.readlines()
            for index,value in enumerate(x):
                if f"title :{work}" in value :
                    k = index
                
            return k
        
        except:
            print("Try again")

    def delete_from_users(self,work):
       
        try:
       
            files = open(f"{self.file_name}\{self.file_name}_work.txt", "r")
            lines = files.readlines()
            files = open(f"{self.file_name}\{self.file_name}_work.txt", "w")
            for index,line in enumerate(lines):
                    
                if index == self.count_user(work):
                    continue
                else :
                    files.write(line)
       
        except:
            print("Try again")


    def get_completed_notcomplet_work(self,status):
        try:
            files = open(f"{self.file_name}\{self.file_name}_work.txt", "r")
            x = files.readlines()
            for index,value in enumerate(x):
                if f"status :{status}" in value :
                    print(value)
                else :
                    continue
        except:
            print("Try again")
def work(file_name):

    try:
        
        work_file = filecontrols(file_name)
        
        print("1)Add work")
        print("2)Delete work")
        print("3)Change work")
        print("4)Get work")
        print("5)Finish work ")
        
        while True:

            user_input = input("What do you do ? :")
            
            if user_input == '1':
                work_file.add_work()
            
            elif user_input == '2':
                input_work = input("Enter the work :")
                work_file.delete_work(input_work)
            
            elif user_input == '3':
                input_work = input("Enter the work :")
                work_file.change_work(input_work)
            
            elif user_input == '4':
                work_file.get_work()
            
            elif user_input == 'cwd':
                print(os.getcwd())
            
            elif user_input == '5':
                break
    
    except :
        print("Try again")
