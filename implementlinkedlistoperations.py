class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None



class LinkedList:
    
    def __init__(self):  
        self.head = None
        self.size=0
    def insert(self,new_data):
        
        new_node=Node(new_data)
        if self.head is None: 
            self.head = new_node 
            return
        last = self.head 
        while (last.next): 
            last = last.next
        last.next =  new_node
        self.size=self.size+1
        
    def display(self): 
        temp = self.head 
        while (temp): 
            print(temp.data,end=" ") 
            temp = temp.next
    def remove(self,key):
        temp=self.head
        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                return
        while(temp is not None): 
            if temp.data == key: 
                break 
            prev = temp 
            temp = temp.next
        if(temp == None): 
            return 
        prev.next = temp.next 
        temp = None
    def Search(self,x):
        current=self.head
        while current != None: 
            if current.data == x: 
                return "true"
            current=current.next
        return "false"
    def insertIndex(self,position,data):
        if(position==0):
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
        elif(position>self.size):
            return
        elif(position==self.size-1):
            self.insert(data)
        else:
            current=self.head
            count=0
            while(current!=None):
                if(count==position-1):
                    break
                else:
                    count=count+1
                    current=current.next
            newnode=Node(data)
            newnode.next=current.next
            current.next=newnode







### write LinkedList class above this line ##

if __name__ == "__main__": 
    test_cases=int(input()) # number of test cases
    myList=LinkedList()

    while(test_cases>0):
        instruction=int(input()) # current instruction
        ####
        # 1 means insertion
        # 2 means remove value
        # 3 means search value
        # 4 means insert at particular index
        # 5 means display entire list
        ####

        if(instruction==1): 
            val=int(input())
            print(f'Insert: {val}')
            myList.insert(val)
        elif (instruction==2):
            val=int(input())
            print(f'Delete: {val}')
            myList.remove(val)
        elif (instruction==3):
            val=int(input())
            print(f'Search for {val}. Found: {myList.Search(val)}')
        elif(instruction==4):
            index=int(input())
            val=int(input())
            print(f'Insert {val} at index {index}')
            myList.insertIndex(index,val)
        elif(instruction==5):
            print('Display:')
            myList.display()
            print()
        
        test_cases=test_cases-1

        
         
           
            
        
            
            
        
            
            
        
              
             
              
        
             
        
        

        
