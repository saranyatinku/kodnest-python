class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


class PlacementManager:
    def __init__(self):
        self.students = []
    
    def add_student_profile(self, student_profile):
        self.students.append(student_profile)
    
    def filter_students_by_course(self, search_course):
        matching_students = [
            student for student in self.students
            if student.course.lower() == search_course.lower()
        ]
        return matching_students


try:
    manager = PlacementManager()
    num_students = int(input())
    
    for i in range(num_students):
        student_id = int(input().strip())  # missing
        name = input().strip()             # missing
        course = input().strip()
        profile = StudentProfile(student_id, name, course)
        manager.add_student_profile(profile)
    
    search_course = input().strip()

    # Filter and display the matching students
    results = manager.filter_students_by_course(search_course)
    if results:
        for student in results:
            print(student)
    else:
        print(f"No students found for course: {search_course}")
        
except Exception as e:
    pass