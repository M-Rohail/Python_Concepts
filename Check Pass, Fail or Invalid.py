# Write a program to check if a student passed, failed, or the entered marks is invalid.

# Get integer input marks.
# Check if the mark is less than 0 or greater than 100. If it's True, print Invalid Marks.
# Check if the mark is greater than 40. If it's True, print Pass.
# Else, print Fail.
marks = int(input("Enter the marks:"))
mark = int(input("Enter the marks:"))
if mark < 0 or mark > marks:
    print("Invalid Marks")
elif mark > 40:
    print("Pass")
else:
    print("Fail")
