import random

def load_student_ids(Roll_Numbers):
    try:
        with open(Roll_Numbers, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file '{Roll_Numbers}' does not exist.")
        return []

def select_students_for_viva(Roll_Numbers):
    all_students = load_student_ids(Roll_Numbers)
    
    
    if not all_students:
        print("No students found. Please check the file and try again.")
        return
    
    unselected_students = all_students[:]
    
    while True:
        # Reset the list if all students have been picked
        if not unselected_students:
            print("\nAll students have been picked! Resetting the list to start again.\n")
            unselected_students = all_students[:]
        
        print("\nRandomly selecting a student for viva...")
        selected_student = random.choice(unselected_students)
        print(f"Selected student: {selected_student}")
        
        # Remove the selected student
        print(f"Removing the selected student ({selected_student}) from the list.")
        unselected_students.remove(selected_student)
        
        # Show remaining unselected students
        print(f"Remaining unselected students: {unselected_students}")
        
        # Exit option
        if input("Press Enter to select the next student, or type 'q' to quit: ").strip().lower() == 'q':
            break

# Run the function with the file containing student IDs
select_students_for_viva('Roll_Numbers.txt')
