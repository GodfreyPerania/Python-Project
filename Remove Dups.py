#Remove Duplicate
#Godfrey D. Perania
#https://github.com/GodfreyPerania
#gperania@gmail.com

def remove_duplicate(value):
    output = []
    seen = set()
    for value in GF:
        if value not in seen:
                output.append(value)
                seen.add(value)
    return output
#Input Integers
GF = input("Enter a List:")

result = remove_duplicate(a)
print (result)