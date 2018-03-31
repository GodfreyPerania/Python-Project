#Linked List
#Godfrey D. Perania
#https://github.com/GodfreyPerania
#gperania@gmail.com

class Node:

    def __init__(self, data = None):
        self.data = data # Assign data
        self.next = None  # Initialize next as null


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self,data):
        new_node = Node(data)
        GF = self.head
        while GF.next != None:
            GF = GF.next
        GF.next = new_node
    def size(self):
        GF = self.head
        total = 0
        while GF.next != None:
            total +=1
            GF = GF.next
        return total
    def display(self):
        GFF = []
        GF_node = self.head
        while GF_node.next != None:
            GF_node = GF_node.next
            GFF.append(GF_node.data)
        print GFF
    def get(self,index):
        if index >= self.size():
            print "ERROR: 'Get' Index out of range"
            return None
        GF_index = 0
        GF_node = self.head
        while True:
            GF_node = GF_node.next
            if GF_index == index: return GF_node.data
            GF_index += 1
    def erase(self,index):
        if index >= self.size():
            print "ERROR: 'Erase' Index out of range"
            return
        GF_index = 0
        GF_node = self.head
        while True:
            last_node = GF_node
            GF_node = GF_node.next
            if GF_index == index:
                last_node.next = GF_node.next
                return
            GF_index += 1


if __name__ == '__main__':

    mylist =  LinkedList()
    maxitems = input("How many Items do you want to Input: ")
    x = 1
    while mylist.size() < maxitems:
        print "Input No.",x,
        y = input("Enter here:  " )
        mylist.append(y)
        x += 1

    print "ORIGINAL LINKED LIST"
    mylist.display()

    GDP = []
    def reverse():
        while mylist.size() != 0:
            GDP.append(mylist.get(mylist.size()-1))
            mylist.erase(mylist.size()-1)
        print "REVERSED LINKED LIST \n", GDP
    reverse()