name = input("Enter a name ")

for i in range(len(name)-1, -1):
    reverse = name[i]+reverse
    print(i)
print(reverse)