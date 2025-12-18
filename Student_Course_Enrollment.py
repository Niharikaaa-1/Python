# - Design a system where students enroll in courses.
#	Predefined tuple of available courses.
#	A student can choose max 5 courses using a loop.
#	Store selected courses in a list.
#	Prevent duplicate entries using a set comparison.
#	Use string methods:
#	.upper(), .capitalize(), membership operator (in).
#	Use nested loops to allow multiple students to enroll.
#	Final output:
#	Student name
#	Enrolled courses
#	Total count
#	Whether “Python Programming” is selected (membership check)

available_courses = (
    "PYTHON PROGRAMMING",
    "DATA STRUCTURES",
    "WEB DEVELOPMENT",
    "DATABASE SYSTEMS",
    "OPERATING SYSTEMS",
    "MACHINE LEARNING",
    "COMPUTER NETWORKS"
)

print("---- COURSE ENROLLMENT SYSTEM ----")
print("Available Courses:")
for course in available_courses:
    print("-", course.title())

students_data = []   

while True:   
    name = input("\nEnter Student Name: ").capitalize()

    chosen_courses = []     
    chosen_set = set()      

    print("\nSelect up to 5 courses (type 'done' to stop):")

    for i in range(5):   
        course_input = input(f"Course {i+1}: ").upper()

        if course_input == "DONE":
            break

        if course_input not in available_courses:
            print("Invalid course! Please choose from available list.")
            continue

        if course_input in chosen_set:
            print("Duplicate! You already selected this course.")
            continue

        chosen_courses.append(course_input)
        chosen_set.add(course_input)

    students_data.append({
        "name": name,
        "courses": chosen_courses
    })

    more = input("\nAdd another student? (yes/no): ").lower()
    if more != "yes":
        break

print("\n===== ENROLLMENT SUMMARY =====")
for student in students_data:
    print("\nStudent Name:", student["name"])
    print("Enrolled Courses:")

    for c in student["courses"]:
        print(" -", c.capitalize())

    total = len(student["courses"])
    print("Total Courses Selected:", total)

    if "PYTHON PROGRAMMING" in student["courses"]:
        print("Python Programming Selected: YES")
    else:
        print("Python Programming Selected: NO")
