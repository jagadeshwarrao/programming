class Queue:
    def __init__(self,size):
        self.data=[]
        self.front=-1
        self.rear=-1
    def enque(self,ele):
        if(self.rear<=size-1):
            if self.front==-1 and self.rear==-1:
                self.front=0
                self.rear=0
            self.data.append(ele)
            self.rear+=1
    def deque(self):
        if(self.front!=self.rear):
            popped=self.data[self.front]
            self.front+=1
            if(self.front==self.rear):
                self.front=-1
                self.rear=-1
            print("deque:"+str(popped))
            #print(self.data)
        else:
            print("None")
    def peek(self):
        if self.front!=self.rear:
            return self.data[self.front]
    def isEmpty(self):
        if(self.front==self.rear):
            return "true"
        else:
            return "false"
    def isFull(self):
        if(self.rear==(size-1)):
            return "true"
        else:
            return "false"




