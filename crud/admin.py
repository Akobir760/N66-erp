from filemanager import read, write, append, generate_id
from datetime import datetime

class Admin:
    def __init__(self):
        self.path = "data/students.csv"
        self.gpath = "data/groups.csv"
        self.tpath = "data/teachers.csv"
        


    def create_student(self):
        login = input("Enter student's login: ")
        password = input("Enter student's password: ")
        created_at = datetime.now()
        student_id = generate_id(self.path)
        s_group = 0
        balance = 0
        student_data = [student_id,login,password,s_group,balance,created_at]
        append(path=self.path, data=student_data)


    def del_student(self):
        student_id = int(input("Enter student's id: "))
        file_data = read(path=self.path)
        for data in file_data:
            if int(data[0]) == student_id:
                file_data.remove(data)
        
        write(path=self.path, data=file_data)

    
    def s_to_group(self):
        student_id = int(input("Enter student's id: "))
        group = input("Enter group id: ")
        file_data = read(path=self.path)
        for data in file_data:
            if int(data[0]) == student_id:
                data[3] = group
                print(f"Student is added to {group}! ")
            
        write(path=self.path, data=file_data)

    
    def search_student(self):
        s_id = int(input("Enter student id: "))
        file_data = read(path=self.path)
        for data in file_data:
            if int(data[0]) == s_id:
                print(f"ID: {data[0]}, Username: {data[1]}, Password: {data[2]}, Group: {data[3]}, Balance: {data[4]}, Created at: {data[5]}")
                break
        else:
            print("Student can not find!")


    def add_balance(self):
        payment_id = generate_id(path="data/payments.csv")
        s_id = int(input("Enter student's id: "))
        amount = int(input("Enter balance amount: "))
        payed_at = datetime.now()
        payment_data = [payment_id,s_id,amount,payed_at]
        append(path="data/payments.csv", data=payment_data)


    def upgrade_s(self):
        s_id = int(input("Enter student's id: "))
        n_username  = input("Enter new username: ")
        n_password = input("Enter new password: ")
        file_data = read(path=self.path)
        for data in file_data:
            if int(data[0]) == s_id:
                data[1] = n_username 
                data[2] = n_password  
                write(path=self.path, data=file_data)
                print("Upgrade is finish!")
                
        


    def create_group(self):
        group_id = generate_id(path=self.gpath)
        group_name = input("Enter group's name: ")
        total_lessons = int(input("Enter total lessons: "))
        started_at = input("Enter starting time: ")
        ended_lessons = 0
        teacher_id = int(input("Enter teacher's id: "))
        group_data = [group_id,group_name,total_lessons,ended_lessons,teacher_id,started_at]
        append(path=self.gpath, data=group_data)
        print(f"Group {group_name} is create!")


    def upgrade_group(self):
        g_id = int(input("Enter group's id: "))
        n_group_name = input("Enter group's name: ")
        n_total_lessons = int(input("Enter total lessons: "))
        n_started_at = input("Enter starting time: ")
        n_ended_lessons = int(input("Enter number of ended lessons: "))
        file_data = read(path=self.gpath)
        for data in file_data:
            if int(data[0]) == g_id:
                data[1] == n_group_name 
                data[2] == n_total_lessons 
                data[3] ==n_ended_lessons 
                data[5] == n_started_at
                print("Group is upgrade!")

    
    def del_group(self):
        g_id = int(input("Enter group's id: "))
        filedata = read(path=self.gpath)
        for data in filedata:
            if int(data[0]) == g_id:
                filedata.remove(data)
                print("Group is delete!")
                
            write(path=self.gpath, data=filedata)
        else:
            print("Group can not find!")


    def create_teacher(self):
        teacher_id = generate_id(path=self.tpath)
        teacher_name = input("Enter teacher's username: ")
        password = input("Enter teacher's password: ")
        full_name = input("Enter teacher's fullname: ")
        experience = int(input("Enter teacher's experience"))
        group = 0
        teacher_data = [teacher_id,teacher_name,password,full_name,experience,group]
        append(path=self.tpath, data=teacher_data)

    
    def del_teacher(self):
        t_id = int(input("Enter teacher's id: "))
        file_data = read(path=self.tpath)
        for data in file_data:
            if int(data[0]) == t_id:
                file_data.remove(data)
                print("Teacher is delete!")
                write(path=self.tpath, data=file_data)
                break

        else:
            print("Teacher can not find!")

        
    def t_upgrade_login(self):
        teacher_id = int(input("Etner teacher's id: "))
        n_username = input("Enter new username: ")
        n_password = input("Enter new password: ")
        file_data = read(path=self.tpath)
        for data in file_data:
            if int(data[0]) == teacher_id:
                data[1] = n_username 
                data[2] = n_password
                print("Login is upgrade!")
            write(path=self.tpath, data=file_data)
            break

        else:
            print("Teacher can not find!")


    def t_upgrade_fn_ex(self):
        t_id = int(input("Enter teacher's id: "))
        n_fullname = input("Enter new fullname: ")
        n_experience = input("Enter new experience: ")
        file_data = read(path=self.tpath)
        for data in file_data:
            if int(data[0]) == t_id:
                data[3] = n_fullname 
                data[4] = n_experience
                print("Changes is save!")
            write(path=self.tpath, data=file_data)

        else:
            print("Teacher can not find!")


    def t_upgrade_group(self):
        t_id = int(input("Enter teacher's id: "))
        n_group = input("Enter new group: ")
        file_data = read(path=self.tpath)
        for data in file_data:
            if int(data[0]) == t_id:
                data[5] = n_group
                print("Changes is save!")
            write(path=self.tpath, data=file_data)

        else:
            print("Teacher can not find!")

    
    def teacher_group(self):
        t_id = int(input("Enter teacher's id: "))
        G_name = input("Enter group's id: ")
        file_data = read(path=self.tpath)
        for data in file_data:
            if int(data[0]) == t_id:
                data[5] == G_name
            print("Teacher's group is save!")
            write(path=self.tpath, data=file_data)
            break
            
        else:
            print("Teacher can not find!")


admin1 = Admin()




    
