biology=float(input("Please input your Biology score:"))
chemistry=float(input("Please input your Chemistry score:"))
physics=float(input("Please input your Physics score:"))
if biology<40:
   print("Fail")
if chemistry<40:
   print("Fail")
if physics<40:
   print("Fail")
else:
   score=((biology+chemistry+physics)/3)
   if score >=70:
       print("first")
   elif score>=60:
       print("2.1")
   elif score>=50:
       print("pass")
   elif score>=40:
        print("pass")
   else:
        print("fail")