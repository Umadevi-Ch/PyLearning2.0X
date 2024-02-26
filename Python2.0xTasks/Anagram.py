str1 = input("Enter first string ")
str2 = input("Enter second string ")

str1 = sorted(str1.lower())
str2 = sorted(str2.lower())

def isAnagram():
    if(str1==str2):
        return ("The strings are anagrams")
    else:
        return ("The strings are not anagrams")

print((isAnagram()))
