# Get the number of grades user will input
num_grades = int(input("Enter the number of grades: "))

total = 0

# Loop to get each grade from user
for i in range(num_grades):
    grade = float(input(f"Enter grade {i+1}: "))
    total += grade

# Calculate average
average = total / num_grades

# Output average
print(f"Your average grade is: {average}")
