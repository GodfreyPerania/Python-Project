#Palindrome Checker
#Godfrey D. Perania
#https://github.com/GodfreyPerania
#gperania@gmail.com

GF = "Dennis, Nell, Edna, Leon, Nedra, Anita, Rolf, Nora, Alice, Carol, Leo, Jane, Reed, Dena, Dale, Basil, Rae, Penny, Lana, Dave, Denny, Lena, Ida, Bernadette, Ben, Ray, Lila, Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina, Lily, Arne, Bette, Dan, Reba, Diane, Lynn, Ed, Eva, Dana, Lynne, Pearl, Isabel, Ada, Ned, Dee, Rena, Joel, Lora, Cecil, Aaron, Flora, Tina, Arden, Noel, and Ellen sinned."
print GF

#I use replace to remove all spaces, since remove can't be used in string

GF = GF.replace(" ","")
GF = GF.lower()

#convert the string into list
GF_list = list(GF)


#reverse the list
GF_rev = GF_list[::-1]

#conditional statement
if GF_rev == GF_list:
    print ("\n\n\n YESH! IT'S A PALINDROME")
else:
    print ("\n\n\n NAH! IT'S NOT PALINDROME")
