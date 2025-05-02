# Supera admin menu:
#     1. Show all admins
#     2. Create admin
#     3. Delete admin
#     4. Show statistics
#     5. Logout

import csv
from datetime import datetime
from filemanager import read, write, append, generate_id

s_admin_name = "s_admin"
s_admin_password = "s_admin"


def show_all_admins():
    with open(file=f"data/admins.csv", mode="r", encoding="UTF-8") as file:
        file_data = csv.reader(file)
        for data in file_data:
            print(f" ID: {data[0]}, Fullname: {data[1]}, Username: {data[2]}, Password: {data[3]}, Created at: {data[4]}")


def create_admin():
    admin_username = input("Enter admin's username: ")
    admin_password = input("Enter admin's pasword: ")
    admin_id = generate_id("data/admins.csv")
    admin_full_name = input("Enter admin's full name: ")
    created_at = datetime.now()
    data = [admin_id,admin_full_name,admin_username,admin_password,created_at]
    append(path="data/admins.csv", data=data)


def del_admin():
    admin_id = int(input("Enter admin's id: "))
    file_data = read(path='data/admins.csv')
    for data in file_data:
        if int(data[0]) == admin_id:
            file_data.remove(data)
            print("Admin is delete!")

    write(path="data/admins.csv", data=file_data)


def show_statistics():
    t_data = read("data/teachers.csv")
    a_data = read("data/admins.csv")
    s_data = read("data/students.csv")

    print(f"Number of admins: {len(a_data)}, number of teachers: {len(t_data)}, number of students: {len(s_data)}.")


