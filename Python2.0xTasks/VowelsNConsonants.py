#Count Vowels and Consonants in a string

str = input("Enter a string ")

vowels = 0
consonants = 0

for i in str:
    if (i.lower() in 'aeiou'):
        vowels += 1
    else:
        consonants += 1

print("Total Number of Vowels in this String =", vowels)
print("Total Number of Consonants in this String =", consonants)