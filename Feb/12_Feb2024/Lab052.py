browser = str(input("Enter the browser name \n"))
browser = browser.lower()
match browser:
    case "Chrome":
        print("Chrome code is executed!")
    case "Fire fox":
        print("Firefox code is executed!")
    case _:
        print("No browser Found!")
