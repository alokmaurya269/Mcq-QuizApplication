# today i am going to learn some concepts of python like function, loops,conditional statements etc
# by making a student mark analyzer 

students = {}  # for storing student data

# percentage calculation function

def percentage_calculator(marks):
    total_marks = sum(marks)
    percentage = (total_marks/ len(marks))
    return percentage

def grade_calculator(percentage):    # now guys we will define grades how our teacher assing grades to us hehehe
    if percentage >= 95:
        return "A+"
    elif percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B+"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C+"
    elif percentage >= 50:
        return "C"
    else:
        return "D"
       

     #function to add student data
def add_student():
    roll = input("Enter your roll number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter your Name: ")

    marks = []

    subjects = int(input("Enter number of subjects: "))
         
    for i in range(subjects):
        mark = int(input(f"Enter marks of your subject {i+1}: "))
        marks.append(mark)


    percentage = percentage_calculator(marks)
             
    grade = grade_calculator(percentage)

    students[roll] = {
       "Name" : name,
       "Marks": marks,
       "Percentage": percentage,
       "Grade": grade
}


    print("Student added successfully!")

#function to view student data
def display_students():
    if not students:
        print("No Student Data Available!")
        return

    print("\n-----------Student Data-----------")
    for roll, data in students.items():
      print(f"\nRoll Number: {roll}")
      print(f"Name: {data['Name']}")
      print(f"Marks: {data['Marks']}")
      print(f"Percentage: {data['Percentage']:.2f}%")
      print(f"Grade: {data['Grade']}")
#   --------- while loop for menu ---------

while True:
    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
      add_student()
    elif choice == "2":
      display_students()
    elif choice == "3":
      print("👋 Exiting program. Thank you!")
      break
    else:
      print("❌ Invalid choice. Try again.")


