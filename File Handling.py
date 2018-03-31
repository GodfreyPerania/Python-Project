#File Handling
#Godfrey D. Perania
#https://github.com/GodfreyPerania
#gperania@gmail.com

text_file = open("text.txt",'w')
text_file.write("Hi! This is a Python Program.")
text_file.close()
text_file = open("text.txt",'a')
text_file.write("Welcome to PUP-College of Engineering")
text_file.close()