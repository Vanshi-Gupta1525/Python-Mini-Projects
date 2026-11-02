students = []
print("===========STUDENT MANAGEMENT SYSTEM===========")
while True:
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. View Students")
    print("5. Search Student")
    print("6. Exit")
    
    choice = input("Enter Choice (1-6): ")
    if choice == "6":
        print("System Closed !")
        break
    
    if choice == "1":
        print("======Enter Student Details======")
        student_name = input("Enter Name: ")
        student_roll_no = int(input("Enter Roll no: "))
        student_contact = int(input("Enter contact: "))
        student_course = input("Enter Course: ")
        
        item_detail = {"Name":student_name,
                   "Roll_No":student_roll_no,
                   "Contact":student_contact,
                   "Course":student_course }
        
        students.append(item_detail)
        
        print("Student add successfully.")
        print("---------------------------")
        
    elif choice == "2":
        roll = int(input("Enter Roll No: "))
        found = False
        
        for student in students:
            
            if student["Roll_No"] == roll:
                students.remove(student)
                
                print("------Student Delete successfully-------")
                print()
                found = True
                break
        
        if not found:
            print("Student Not Found!")
            
            
    elif choice == "3":
        search_id = int(input("Enter student roll no : "))
        
        search_found = False
        
        for student in students:
            
            if student['Roll_No'] == search_id:
                
                search_found = True
                
                print("--------Student Details---------")
                print(f'Name: {student['Name']}')
                print(f'Roll no : {student['Roll_No']}')
                print(f'Contact : {student['Contact']}')
                print(f'Course : {student['Course']}')
                print("-----------------------------------------\n")
                
                print("\n Enter New Details (Leave blank if you eant old detail !)")
                
                new_name = input("Enter Name : ")
                new_roll_no = (input("Enter Roll No : "))
                new_contact = (input("Enter Contact : "))
                new_course = input("Enter Course : ")
                
                if new_name:
                    student["Name"] = new_name
                    
                if new_roll_no:
                    student["Roll_No"] = int(new_roll_no)
                    
                if new_contact:
                    student["Contact"] = int(new_contact)
                    
                if new_course:
                    student["Course"] = new_course
                    
                print("\nRecord Updated Successfully!")
                
                print("\n-------- Updated Student Details --------") 
                for key, value in student.items(): 
                    print(f"{key}: {value}")
                    
                print("------------------------------------------")
                break
        if not search_found:
            print("Error: Student Roll No. Not Found!")
        
            
    
    elif choice == "4":
        
        if len(student) == 0:
            print("List is Empty!")
            
        else:
            print("----Students Details-----")
            for student in students: 
                for key, value in student.items():
                    print(f"{key}: {value}")
                print("---------------------------------------")
        
            
    elif choice == "5":
        
        roll = int(input("Enter Roll No: "))
        found = False
        print("--------Student Details---------")
        for student in students:
            if student["Roll_No"] == roll:
                for key, value in student.items():
                    print(f"{key}: {value}")
                print("--------------------------------")
                found = True
                
        if not found:
            print("Student Not Found")
            
            
    else:
        print("Invalid Choice!")
        
    ch = input("Do you want to add more students ? Yes/No : ").lower()
    if ch!= "yes":
        print("Thank You !")
        break
        
        