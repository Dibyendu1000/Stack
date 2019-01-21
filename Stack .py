print('Stack')
#================================================================================
class stack:
    def __init__(self):
        self.LIST=[]
        self.n=0
        self.pos=-1
#====================================================================================================
    def readlist(self):
        self.LIST=[]
        self.pos=-1
        self.n=int(input('Enter the no of elements:'))
        for i in range(self.n):
            self.LIST.append(None)
#======================================================================================================
    def push(self):
       
        if self.pos>=self.n-1:
            print('--------------------')
            print('Stack Overflow')
            print('--------------------')
        else:
            self.pos+=1
            self.LIST[self.pos]=int(input('Enter your value:'))
            
#=========================================================================================================
    def pop(self):
        if self.pos == -1:
            print('STACK UNDERFLOW!!')
        else:
            print('POPED: {}'.format(self.LIST[self.pos]))
            self.pos-=1
    
        
#==========================================================================================================
    def display(self):
        print('------------------------')
        for i in range(self.pos,-1,-1):
            print(self.LIST[i],end=' ')
            print('-------------------------')
#===========================================================================================================
    def choice(self):
        while(True):
            print('1.Entry')
            print('2.Push')
            print('3.Pop')
            print('4.Display')
            print('5.Exit')
            ch=int(input('Enter your choice:'))
            if ch==1:
                self.readlist()
            elif ch==2:
                self.push()
            elif ch==3:
                self.pop()
            elif ch==4:
                if self.pos >=0:
                    self.display()
                else:
                    print('STACK UNDERFLOW!!')
            else:
                break
ob=stack()
ob.choice()
            

            
                
