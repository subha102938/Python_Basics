subject_one_marks = int(input("Subject 1: "))
subject_two_marks = int(input("Subject 2: "))
subject_three_marks = int(input("Subject 3: "))
subject_four_marks = int(input("Subject 4: "))
subject_five_marks = int(input("Subject 5: "))

total_marks = subject_one_marks + subject_two_marks + subject_three_marks + subject_four_marks + subject_five_marks

percentage = total_marks / 5

if (subject_one_marks < 0 or subject_one_marks > 100 or
    subject_two_marks < 0 or subject_two_marks > 100 or
    subject_three_marks < 0 or subject_three_marks > 100 or
    subject_four_marks < 0 or subject_four_marks > 100 or
    subject_five_marks < 0 or subject_five_marks > 100):

    print("Invalid Marks")

else:
    if (subject_one_marks < 35 or subject_two_marks < 35 or
        subject_three_marks < 35 or subject_four_marks < 35 or
        subject_five_marks < 35):

        result = "FAIL"

    else:
        result = "PASS"

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    print("Total Marks:", total_marks)
    print("Percentage:", percentage, "%")
    print("Grade:", grade)
    print("Result:", result)

    if result == "PASS" and percentage > 90:
        print("Performance: Outstanding Performance")
