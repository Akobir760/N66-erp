from filemanager import FileManager

class Student(FileManager):
    def __init__(self, filepath):
        super().__init__(filepath)


    def show_groups(self):
        rows = self.read()
        for row in rows:
            print(row)

    def upload_homework(self):
        reader = FileManager(file_path="homework.csv")
        reader.read()
        data = input("enter your homework id")
        reader.write(data)
        print("Your homework has been uploaded")



    def show_all_my_attendance(self):
        show = FileManager(file_path="attendance.csv")
        rows = show.read()
        for row in rows:
            print(row)

    def show_all_my_balance(self):
        balance = FileManager(file_path="balance.csv")
        rows = balance.read()
        for row in rows:
            print(row)

    def payment(self):
        reader = FileManager(file_path="payment.csv")
        rows = reader.read()
        balance = int(input("enter your balance :"))
        rows.writer(balance)
        print("Your balance has been paid")