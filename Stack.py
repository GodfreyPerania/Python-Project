#Stack
#Godfrey D. Perania
#https://github.com/GodfreyPerania
#gperania@gmail.com

class Stack:
    def __init__(self):
        print "LIST MANIPULATION USING STACK"
        self.items = input("\nEnter a list of strings:")
        self.items = list(self.items)

    def sort(self):
        return sorted(self.items)

    def reverse(self):
        return self.items[::-1]

    def isEmpty(self):
        return self.items == []

    def insert(self,value,item):
        return self.items.insert(value,item)

    def push(self, item):
        return self.items.append(item)

    def append(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    GF = Stack()
    def qt():

        GFF = 0
        print ("\n1. SORT THE LIST \n2. REVERSE THE LIST \n3. ADD AN ITEM \n4. INSERT AN ITEM \n5. GET THE SIZE \n6. COUNT THE PALINDROME")
        x = input("\nChoose the action you want: ")
        if x == 1:
            print "SORTED VERSION: ",GF.sort()
        elif x == 2:
            GPFF = []
            while GF.isEmpty() == False:
                GPFF.append(GF.peek())
                GF.pop()
            print "REVERSED VERSION:", GPFF
            return 0

        elif x == 3:
            GFFF = input("\tEnter the word you wanna add: ")
            GF.push(GFFF)
            print "\t", GF.items
        elif x == 4:
            GFFF = input("\tInsert: ")
            GP = input("\tIndex: ")
            GF.insert(GP, GFFF)
            print "\t",GF.items
        elif x == 5:
            print "SIZE:",GF.size()
        elif x == 6:
            while GF.isEmpty() == False:
                if GF.peek() == GF.peek()[::-1]:
                    GFF += 1
                GF.pop()
            print "TOTAL PALINDROME: ", GFF
            return 0


        return qt()
    qt()