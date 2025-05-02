from crud import auth, s_admin, admin, teacher



def Auth_menu():
    print("1. Login \n2. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        res = auth.Auth()
        if res == "admin":
            return admin_menu()
        elif res == "student":
            return students_menu()
        elif res == "teacher":
            return teacher_menu()
        elif res == "s_admin":
            return s_admin_menu()
        else:
            print("Invalid password or username!")
            return Auth_menu()
        
    elif choice == 2:
        print("Exiting...")
        return
    else:
        print("Invalid choice!")
        return Auth_menu()


def teacher_menu():
    print("""
    1. My groups
    2. Show group (by id)
    3. Start the lesson (group id) 
    4. Homework CRUD (lesson id)
    5. Logout
    """)
    choice = input("Enter your choice:")
    if choice == 1:
        teacher.teacher1.my_groups()
    elif choice == 2:
        teacher.teacher1.show_group()
    elif choice == 3:
        teacher.teacher1.start_lesson()
    elif choice == 4:
        print("1. Create homework \n2. Delete homework")
        h_choice = int(input("Enter your choice: "))
        if h_choice == 1:
            teacher.teacher1.create_homework()
        elif h_choice == 2:
            teacher.teacher1.delete_homework()
        else:
            print("Invalid choice!")
        return teacher_menu()
    elif choice == 5:
        print("Exiting...")
        return
    else:
        print("Invalid choice")
    return teacher_menu()


def students_menu():
    print("""
    1. Show groups
    2. Upload homework (id)
    3. Show my all attendance
    4. Show my balance
    5. Payment
    6. Logout
    """)
    choice = input("Enter your choice:  ")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    else:
        print("Invalid choice")


def admin_menu():
    print("""
          Admin menu:
    1. Students CRUD 
    2. Groups CRUD 
    3. Student to group
    4. Search student 
    5. Add to balance
    6. Teacher CRUD
    7. Teacher to group
    8. Exit
""")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(f"1. Create student \n2. Delete student \n3. Upgrade student ")
        crud_choice = int(input("Enter your choice number: "))
        if crud_choice == 1:
            admin.admin1.create_student()
        elif crud_choice == 2:
            admin.admin1.del_student()
        elif crud_choice == 3:
            admin.admin1.upgrade_s()
        else:
            print("Invalid choice!")
        return admin_menu()
    elif choice == 2:
        print("1. Create group \n2. Delete group\n 3. Upgrade group")
        g_choice = int(input("Enter your choice: "))
        if g_choice == 1:
            admin.admin1.create_group()
        elif g_choice == 2:
            admin.admin1.del_group()
        elif g_choice == 3:
            admin.admin1.upgrade_group()
        else:
            print("Invalid choice!")
        return admin_menu()
    elif choice == 3:
        admin.admin1.s_to_group()
    elif choice == 4:
        admin.admin1.search_student()
    elif choice == 5:
        admin.admin1.add_balance()
    elif choice == 6:
        print("1. Create teacher \n2. Delete teacher \n3. Upgrade teacher")
        t_choice = int(input("Enter your choice: "))
        if t_choice == 1:
            admin.admin1.create_teacher()
        elif t_choice == 2:
            admin.admin1.del_teacher()
        elif t_choice == 3:
            print("1. Upgrade login \n 2. Upgrade fullname and experience \n3. Upgrade group")
            u_choice = int(input("Enter your choice:"))
            if u_choice == 1:
                admin.admin1.t_upgrade_login()
            elif u_choice == 2:
                admin.admin1.t_upgrade_fn_ex()
            elif u_choice == 3:
                admin.admin1.t_upgrade_group()
            else:
                print("Invalid choice!")
            return admin_menu()
        else:
            print("Invalid choice!")
        return admin_menu()
    elif choice == 7:
        admin.admin1.teacher_group()
    elif choice == 8:
        print("Good bye!")
        return Auth_menu()
    else:
        print("Invalid choice!")
    return admin_menu()
    

def s_admin_menu():
    print("""Supera admin menu:
    1. Show all admins
    2. Create admin
    3. Delete admin
    4. Show statistics
    5. Logout
""")
    
    choice = int(input("Enteer your choice: "))
    if choice == 1:
        s_admin.show_all_admins()
    elif choice == 2:
        s_admin.create_admin()
    elif choice == 3:
        s_admin.del_admin()
    elif choice == 4:
        s_admin.show_statistics()
    elif choice == 5:
        print("Good bye!")
        return Auth_menu()
    else:
        print("Invalid choice!")
    return s_admin_menu()


if __name__ == "__main__":
    Auth_menu()