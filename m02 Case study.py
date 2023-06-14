###Clyde Kershaw
### M02 Lab Case Study
### This application will contain a Python app that will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll

last_name = ""
first_name = ""
gpa = 0


while last_name != "ZZZ":
    last_name = input ("Enter your Last name: ")
    if last_name == "ZZZ":
        break
    first_name = input ("Enter your First name: ")
    gpa = float(input("Enter your GPA:"))
    if gpa > 3.5:
        print (first_name, last_name, "with GPA of", gpa, "has made the Dean's List")
    if gpa > 3.25:
        print (first_name, last_name, "with GPA of", gpa, "has made the honor roll")


