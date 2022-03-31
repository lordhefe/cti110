Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
wage = 20
hours = 40
weeks = 52
salary = wage * hours * weeks
SyntaxError: multiple statements found while compiling a single statement

=================== RESTART: C:/Users/boyert5394/firstprog.py ==================
Enter first number: 5.2
Enter first number: 5
the total is: 10.2
x=9
y=10.2
total=x+9
total
18
type(total)
<class 'int'>
str(total)
'18'


x=9
x
9
x=12
5/2
2.5
5//2
2
5/3
1.6666666666666667
5//3
1
7*2
14
5/2
2.5
5/2
2.5
5%2
1
6%2
0
5**
SyntaxError: invalid syntax
3**3
27
print("5*5=", 5*5)
5*5= 25
print("the price is $", 500)
the price is $ 500
print("the price is $", 500,sep="")
the price is $500
print("the total is:", total)
the total is: 18

=================== RESTART: C:/Users/boyert5394/firstprog.py ==================
Enter first number: 4
Enter first number: 5
the total is:	9.0

=================== RESTART: C:/Users/boyert5394/firstprog.py ==================
Enter the first number: 1
Enter the second number: 1
the total is:	2.0

=================== RESTART: C:/Users/boyert5394/firstprog.py ==================
Enter the first number: 
=================== RESTART: C:/Users/boyert5394/firstprog.py ==================
Enter the first number: 5
enter the second number: Enter the second number: 5
the total is:	10.0
# scores= {99,98,99,89}
score=[]
#lists are
#1.chngable/mutable

#2. 0 index
scores[2]=100
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    scores[2]=100
NameError: name 'scores' is not defined. Did you mean: 'score'?
scores=[]
scores.append(45)
scores
[45]
scores.extend([56,85])
scores
[45, 56, 85]
scores.pop[]
SyntaxError: invalid syntax
scores.append(54)
scores.pop()
54
scores.remove(85)
scores
[45, 56]
scores.pop(1)
56
