from student import Student

def Auth_menu():
    choice = int(input("Enter your choice: "))
    if choice == 1:
        pass
    elif choice == 2:
        pass
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
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    else:
        print("Invalid choice")
        teacher_menu()


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


