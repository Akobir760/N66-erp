import csv

from filemanager import read, write, append

class Student:
    def __init__(self, filepath):
        self.filepath = filepath

    def show_groups(self):
        rows = read(self.filepath)
        if rows:
            for row in rows:
                print(f"groups : {row}")
        else:
            print("No groups found")

    def upload_homework(self):
        data = input("enter your homework id")
        write(self.filepath, data)
        print("Your homework has been uploaded")


    def show_all_my_attendance(self):
        rows = read(self.filepath)
        if rows:
            for row in rows:
                print(f"attendance : {row}")
        else:
            print("you did not enter any lesson.")

    def show_all_my_balance(self):
        rows = read(self.filepath)
        if not rows:
            print("your balance : 0")
        else:
            for row in rows:
                print(f"your balance : {row}")

    def payment(self):
        balance = int(input("enter your balance :"))
        append(self.filepath,[balance])
        print("Your balance has been paid")