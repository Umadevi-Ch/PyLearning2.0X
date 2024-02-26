browser = str(input("Enter the browser name:\n"))
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome code executed")
    case "Firefox":
        print("Firefox code executed")
    case "google":
        print("Google browser executed")
    case browser if browser == "fb":
        print("you are entered Facebook")
    case browser if browser == "insta":
        print("you are entered Instagram")
    case _:
        print("No browser found")
