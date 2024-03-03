try:
    with open("TestData", 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError as fnferror:
    print(fnferror)
finally:
    file.close()