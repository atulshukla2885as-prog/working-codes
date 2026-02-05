anubahvname = input("Enter student name: ")

marks1 = int(input("Enter marks in Subject 1: "))
marks2 = int(input("Enter marks in Subject 2: "))
marks3 = int(input("Enter marks in Subject 3: "))

total = marks1 + marks2 + marks3
average = total / 3

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

print("\n--- Result ---")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)
