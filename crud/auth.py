from filemanager import read, write, append


def Auth():
    s_admin_name = "s_admin"
    s_admin_password = "s_admin"

    user_name = input("Enter your user name: ")
    password = input("Enter your password: ")

    admin_data = read("data/admins.csv")
    students_data = read("data/students.csv")
    teachers_data = read("data/teachers.csv")

    if user_name == s_admin_name and password == s_admin_password:
        return "s_admin"

    for data in admin_data:
        if data[2] == user_name and data[3] == password:
            return "admin"

    for data in students_data:
        if data[1] == user_name and data[2] == password:
            return "student"

    for data in teachers_data:
        if data[1] == user_name and data[2] == password:
            return "teacher"
