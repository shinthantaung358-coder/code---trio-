



course_grade = input("Please enter your letter grade for the coruse")

while True:
    if course_grade == "A":
        print("You passed")
        break
    elif course_grade == "B":
        print("You passed")
        break
    elif course_grade == "C":
        print("You passed")
        break

    else:
        print("Keep going .. you cannot pass until you get c or better grade")
        course_grade = input("put in the new letter grade you receive to see if you passed")