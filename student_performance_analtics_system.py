import pandas as pd
import numpy as np


def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"



def calculate_result(avg, attendance):
    if avg >= 35 and attendance >= 75:
        return "Pass"
    else:
        return "Fail"



def main():
    students = []

    subjects = ["Python", "SQL", "HTML", "CSS", "JavaScript"]

    print("=" * 50)
    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 50)

    n = int(input("Enter number of students: "))

    # Get student details
    for i in range(n):
        print("\nEnter details for Student", i + 1)

        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        department = input("Enter Department: ")

        student = {
            "Student_ID": student_id,
            "Name": name,
            "Department": department
        }

        for subject in subjects:
            mark = float(input("Enter " + subject + " marks: "))
            student[subject] = mark

        attendance = float(input("Enter Attendance percentage: "))
        student["Attendance"] = attendance

        students.append(student)

    
    df = pd.DataFrame(students)

    print("\n========== STUDENT DATA ==========\n")
    print(df.to_string(index=True))

    
    df["Total"] = np.sum(df[subjects].values, axis=1)
    df["Average"] = np.mean(df[subjects].values, axis=1).round(2)

    grades = []
    results = []

    for i in range(len(df)):
        avg = df.loc[i, "Average"]
        attendance = df.loc[i, "Attendance"]

        grade = calculate_grade(avg)
        result = calculate_result(avg, attendance)

        grades.append(grade)
        results.append(result)

    df["Grade"] = grades
    df["Result"] = results

    
    print("\n========== STUDENT PERFORMANCE ==========\n")

    columns = ["Student_ID", "Name", "Total",
               "Average", "Grade", "Result"]

    print(df[columns].to_string(index=True))

    
    print("\n========== OVERALL ANALYSIS ==========\n")

    print("Total Students:", len(df))
    print("Highest Average:", df["Average"].max())
    print("Lowest Average:", df["Average"].min())
    print("Class Average:", round(df["Average"].mean(), 2))

    passed = 0
    failed = 0

    for i in range(len(df)):
        if df.loc[i, "Result"] == "Pass":
            passed = passed + 1
        else:
            failed = failed + 1

    print("Passed Students:", passed)
    print("Failed Students:", failed)

    
    top_average = df["Average"].max()

    print("\n========== TOP PERFORMER ==========\n")

    for i in range(len(df)):
        if df.loc[i, "Average"] == top_average:
            print("Name:", df.loc[i, "Name"])
            print("Average:", df.loc[i, "Average"])
            print("Grade:", df.loc[i, "Grade"])

    
    print("\n========== SUBJECT-WISE ANALYSIS ==========\n")

    for subject in subjects:
        print(subject, "Average:", round(df[subject].mean(), 2))


main()
