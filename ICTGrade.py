name=(input("Enter student name:"))
homework=float(input("Please input homework score:"))
assessment=float(input("Please input assessment score:"))
final=float(input("Please input final score:"))

def grade(homework,assessment,final):
    average=((homework+assessment+final)/3)
    if average >=70:
        print("Grade A")
    elif average>=60:
        print("Grade B")
    elif average>=50:
        print("Grade C")
    elif average>=40:
        print("Grade D")
    else:
        print("Grade Fail")
    return average
    
result = grade(homework,assessment,final)
print (result)
