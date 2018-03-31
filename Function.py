#Function
#Godfrey D. Perania
#https://github.com/GodfreyPerania
#gperania@gmail.com


G = "Hello World"
P = "HoRaY FoR ToDAy"

#ALL CHARACTERS IN UPPERCASE
print G.upper()

#ALL CHARACTERS IN LOWER CASE
print G.lower()

#CAPITALIZES THE FIRST CHARACTER OF EACH STRING
print G.title()

#CAPITALIZES THE FIRST CHARACTER OF THE SENTENCE
print G.capitalize()

#ALTERNATES THE SET OF CASE OF CHARACTER; IF CHARACTER IS IN UPPERCASE, IT WILL BE LOWERCASE AND VISE VERSA
print P.swapcase()

#Counts the no. of Uppercase and lowercase letters upon an inputted words
def count():
    a = P
    d = {"UPPER CASE" : 0, "LOWER CASE": 0,"SPACE": 0}
    for c in a:
        if c.isupper():
            d["UPPER CASE"] += 1
        elif c.islower():
            d["LOWER CASE"] += 1
        else:
            pass

    print " NO. of UPPERCASE LETTERS is ", d["UPPER CASE"]
    print " NO. of lowercase letters is ", d["LOWER CASE"]
    return count()

count()
