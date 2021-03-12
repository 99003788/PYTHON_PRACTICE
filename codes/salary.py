salary = int(input("Enter basic Salary:\n"))
da= float((5 * salary)/100)
hra = float((7 * salary)/100)
pf = float((9 * salary)/100)
ta = float((3 * salary)/100)
if salary < 5000:
    netSalary= float(salary + ta + da + hra + pf + (15*salary/100) )
    print("Net Salary = ",netSalary)

elif salary >= 5000 and salary < 8000:
    netSalary= float(salary + ta + da + hra + pf + (25*salary/100) )
    print("Net Salary = ",netSalary)

elif salary >= 8000 and salary < 10000:
    netSalary= float(salary + ta + da + hra + pf + (35*salary/100) )
    print("Net Salary = ",netSalary)   

else:
    netSalary= float(salary + ta + da + hra + pf + (50*salary/100) )
    print("Net Salary = ",netSalary) 

  
