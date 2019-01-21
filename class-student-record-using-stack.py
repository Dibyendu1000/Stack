class Student():
    def __init__(self,n,r,c):
        self.name=n
        self.clas=c
        self.roll=r
    def __str__(self):
        string="Student's Name:"+str(self.name)+"\nRoll No.:"+str(self.roll)+"\nClass:"+str(self.clas)
        return string
class Stack():
    def __init__(self):
        self.n=0
        self.list=[]
        self.pos=-1
    def entry(self):
        self.list=[]
        self.pos=-1
        self.n=int(input('Enter no. of students record:'))
        for i in range(self.n):
            self.list.append(None)
    def push(self):
        if self.pos>=self.n-1:
            print('Stack Overflow')
            
        else:
            n=input("Enter Students' Name:")
            c=input('Enter class:')
            r=int(input('Enter roll no.:'))
            Stud=Student(n,r,c)
            self.pos+=1
            self.list[self.pos]=Stud
            
    def pop(self):
        if self.pos==-1:
            print('Stack Underflow')
        else:
            print('Deleted:',self.list[self.pos])
            self.pos-=1
    def display(self):
        if self.pos==-1:
            print('Stack Underflow')
        else:
            print('Printing the Stack')
            for i in range(self.pos,-1,-1):
                print('-'*10)
                print(self.list[i])
                print('-'*10)
    def choose(self):
        while(True):
            print('1.Entry')
            print('2.Push')
            print('3.Pop')
            print('4.Display')
            print('5.Exit')
            ch=int(input('Enter your choice:'))
            if ch==1:
                self.entry()
            elif ch==2:
                self.push()
            elif ch==3:
                self.pop()
            elif ch==4:
                self.display()
            else:
                break
ob=Stack()
ob.choose()
