# Read marks, attendance and project completion status
marks = int(input())
attendance = int(input())
project = input()

# Check the academic requirements
if marks >= 60 and attendance >= 75:
    # Check the project completion
    if project == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")