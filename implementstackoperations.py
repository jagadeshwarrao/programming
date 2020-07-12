### write your solution below this line ### 

class Stack:
    def __init__(self,size):
        self.data = []
        self.size=size
        self.top = -1
    def push(self, element):
        self.data.append(element)
        self.top = self.top + 1
    def pop(self):
        popped_element = None
        if(self.top>-1):
            popped_element = self.data.pop() 
            self.top = self.top - 1
        return popped_element
    def isEmpty(self):
        if(self.top==-1):
            return 1
        else:
            return 0
    def isFull(self):
        if(self.top==self.size-1):
            return 1
        else:
            return 0
    def peek(self):
        if(self.isEmpty()):
            return
        else:
            return self.data[len(self.data)-1]












if __name__ == "__main__": 
    
    test_cases=int(input()) # number of test cases
    size=int(input()) # size of Stack
    stack=Stack(size) # creating new stack object
    
    while(test_cases>0): 
        instruction=input().split()
        val=0
        if len(instruction)>1:
            val=int(instruction[1])

        instruction=int(instruction[0])
        #####
        # Instruction 1 means Push
        # Instruction 2 means Pop
        # Instruction 3 means Peek
        # Instruction 4 means isEmpty
        # Instruction 5 means isFull
        #####

        if(instruction==1):  
            print(f'push:{val}')
            stack.push(val)

        elif (instruction==2):
            print(f'pop:{stack.pop()}')

        elif (instruction==3):            
            print(f'peek:{stack.peek()}')

        elif(instruction==4):
            print(f'isEmpty:{stack.isEmpty()}')

        elif(instruction==5):
            print(f'isFull:{stack.isFull()}')

        test_cases=test_cases-1 