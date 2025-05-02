from filemanager import read, append, generate_id
from datetime import datetime


class Student:
    def __init__(self):
        self.g_path = "data/groups.csv"

    
    def show_groups(self):
        file_data = read(path=self.g_path)
        for data in file_data:
            print(f" Course name: {data[1]}, started at: {data[-1]}")

    
    def Uploade_homework(self):
        homework_id = generate_id(path="data/s_homework.csv")
        lesson_id = int(input("Enter lesson's id: "))
        student_id = int(input("Enter your id: "))
        homework = input("Enter homework: ")
        uploaded_at = datetime.now()
        homework_data = [homework_id,lesson_id,student_id,homework,uploaded_at]

        append(path="data/s_homework.csv", data=homework_data)


    def show_balance(self):
        student_id = int(input("Enter your id: "))
        file_data = read(path="data/payments.csv")
        all_payment = 0
        for data in file_data:
            if int(data[1]) == student_id:
                    all_payment += int(data[2])
                    print(f" Payment amount: {data[2]}, Payment date: {data[3]}")
        
        print(f"All payments amount: {all_payment}")


    def payment(self):
        payment_id = generate_id(path="data/payments.csv")
        s_id = int(input("Enter student's id: "))
        amount = int(input("Enter balance amount: "))
        payed_at = datetime.now()
        payment_data = [payment_id,s_id,amount,payed_at]
        append(path="data/payments.csv", data=payment_data)
        print("Payment is add!")


student1 = Student()
