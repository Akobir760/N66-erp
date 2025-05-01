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
            print(data)


def create_admin():
    admin_username = input("Enter admin's username: ")
    admin_password = input("Enter admin's pasword: ")
    admin_id = generate_id("data/admins.csv")
    admin_full_name = input("Enter admin's full name: ")
    created_at = datetime.now()
    data = [admin_id,admin_full_name,admin_username,admin_password,created_at]
    append(path="data/admins", data=data)


def del_admin():
    admin_id = int(input("Enter admin's id: "))
    file_data = read(path='data/admins')
    for data in file_data:
        if int(data[0]) == admin_id:
            file_data.remove(data)

    write(path="data/admins.csv", data=file_data)
    print("Admin is delete!")





