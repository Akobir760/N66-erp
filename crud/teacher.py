from filemanager import read, write, append, generate_id
from datetime import datetime


class Teacher:
    def __init__(self):
        self.g_path = "data/groups.csv"
        self.l_path = "data/lessons.csv"
        self.t_home = "data/t_homework.csv"

    
    def my_groups(self):
        teacher_id = int(input("Enter your id: "))
        file_data = read(path=self.g_path)
        for data in file_data:
            if int(data[4]) == teacher_id:
                print(data)

    
    def show_group(self):
        g_id = int(input("Enter  group's id: "))
        file_data = read(path=self.g_path)
        for data in file_data:
            if int(data[0]) == g_id:
                print(f"Id: {data[0]}, group name: {data[1]}, total lessons: {data[2]}, ended lesson: {data[3]}, teacher id: {data[4]}, started at: {data[5]}")


    def start_lesson(self):
        lesson_id = generate_id(path=self.l_path)
        t_id = int(input("Enter teacher's id: "))
        l_title = input("Enter lesson's title: ")
        group_id = int(int(input("Enter group's id: ")))
        g_data = read(path=self.g_path)
        started_at = datetime.now()
        for data in g_data:
            if int(data[0]) == group_id:
                data[3] = int(data[3]) + 2
        
        write(path=self.g_path, data=g_data)

        lesson_data = [lesson_id,t_id,l_title,group_id,started_at]
        append(path=self.l_path, data=lesson_data)


    def create_homework(self):
        homework_id = generate_id(self.t_home)
        lesson_id = int(input("Enter lesson id: "))
        h_text = input("Enter homework text: ")
        given_at = datetime.now()
        deadline = input("Enter homework's deadline: ")

        h_data = [homework_id,lesson_id,h_text,given_at,deadline]

        append(path=self.t_home, data=h_data)


    def delete_homework(self):
        filedata = read(path=self.t_home)
        h_id = int(input("Enter homework id: "))
        for data in filedata:
            if int(data[0]) == h_id:
                filedata.remove(data)
                print("Homework is delete!")

        write(path=self.t_home, data=filedata)


teacher1 = Teacher()