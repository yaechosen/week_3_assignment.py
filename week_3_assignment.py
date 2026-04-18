employees = []
total_salary = 0

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        first = input("Enter first name: ")
        last = input("Enter last name: ")
        
        try:
            salary = int(input("Enter annual salary: "))
        except:
            print("Invalid salary. Try again.")
            continue

        employees.append((first, last, salary))
        total_salary += salary

    elif choice == "2":
        if len(employees) == 0:
            print("No employees entered.")
        else:
            print("\nEmployee List:")
            for emp in employees:
                print(emp[0], emp[1], "-", emp[2])

            print("Total Salary:", total_salary)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
