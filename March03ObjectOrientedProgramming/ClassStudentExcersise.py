class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    class_ = "Student"
    def average(self,test1,test2,test3):
        avg=(test1+test2+test3)/3
        return avg

amber=student("Amber",32)

test1=int(input("Enter test score 1:"))   
test2=int(input("Enter test score 2:")) 
test3=int(input("Enter test score 3:"))      

print("The average score is:",amber.average(test1,test2,test3))