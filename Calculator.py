#Calculator
#Godfrey D. Perania
#https://github.com/GodfreyPerania
#gperania@gmail.com

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Close")

def GF():

    GDP = input("Enter Choice:")

    if GDP == 1:
        a = input("FIRST NUMBER: ")
        b = input("SECOND NUMBER: ")
        add = a + b
        print a, "+", b, "=", add

    elif GDP == 2:
        a = input("FIRST NUMBER: ")
        b = input("SECOND NUMBER: ")
        sub = a - b
        print a, "-", b, "=", sub

    elif GDP == 3:
        a = input("FIRST NUMBER: ")
        b = input("SECOND NUMBER: ")
        multi = a * b
        print a, "*", b, "=", multi

    elif GDP == 4:
        a = input("FIRST NUMBER: ")
        b = input("SECOND NUMBER: ")
        divide = a / b
        print a, "/", b, "=", divide

    elif GDP == 5:
        print ("Close")
        return (0)

    else:
        print ("Invalid Input. Please Try again")
        return GF()

    return GF()


GF()