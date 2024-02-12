# Write a program that calculates and displays the letter grade for a
# given numerical score (e.g..A,B,C,D or F)
# based on the following grade scale:
# input score -89
# output - B
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# If,elif, else

# Step1
# Figure out the inputs
# Input - int
# scale =int(input("Enter the number you got!\n"))

# Step2
# Figure out the Logic
# Print A -> if scale <=100 and >=90
# Step3
# Print the output

scale = int(input("Enter the score you got!\n"))
# if 90 <= scale <= 100:
if scale >= 90 and scale <= 100:
    print("Grade is A")
elif scale >= 80 and scale <= 89:
    print("Grade is B")
elif scale >= 70 and scale <= 79:
    print("Grade is C")
elif scale >= 60 and scale <= 69:
    print("Grade is D")
elif scale >= 0 and scale <= 59:
    print("Grade is F")
else:
    print("Invalid Input")


 