#Dictionaries
#Godfrey D. Perania
#https://github.com/GodfreyPerania
#gperania@gmail.com

print "LET'S NOW COMPUTE YOUR FINAL GRADE!!!"

print "\tGRADING SYSTEM\n\t[enter in decimal percentage]"
G = input("\tQuizzes: ")
D = input("\tExercises: ")
P = input("\tAttendance: ")
GF = {}


def Grades():
    Student = input("\nNAME:")

    a = input("     Enter Quizzes here: ")
    b = input("     Enter Exercises here: ")
    c = input("     Enter Attendance here: ")
    GFF = {"Quiz": list(a), "exercise": list(b), "Attendance": c, "FINAL GRADE": []}

    GFF["Quiz"] = float(sum(a) / len(a))
    GFF["exercise"] = float(sum(b) / len(b))
    GFF["FINAL GRADE"] = GFF["Quiz"] * G + GFF["exercise"] * D + GFF["Attendance"] * P
    GDP = GFF["FINAL GRADE"]
    print "     FINAL GRADE: ", GFF["FINAL GRADE"]
    if GFF["FINAL GRADE"] >= 75:
        print "     CONGRATULATIONS ", Student, ",YOU'VE PASSED THE SUBJECT"
    elif GFF["FINAL GRADE"] <= 74:
        print "\tI'M SORRY", Student, ",YOU'VE FAILED"
    GF[Student] = GDP

    x = input("\n[1] Continue... [2] Print Result     : ")
    if x == 1:
        return Grades()
    elif x == 2:
        print GF  # it returns to a dictionary with the names as keys and the corresponding final grades as the value.

Grades()