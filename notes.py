Python 3.10.4 (v3.10.4:9d38120e33, Mar 23 2022, 17:29:05) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
cti110 = [5,6,7,8,9,4,3]
cti110
[5, 6, 7, 8, 9, 4, 3]
len(cti110)
7
insert(2)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    insert(2)
NameError: name 'insert' is not defined
cti.pop
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    cti.pop
NameError: name 'cti' is not defined
cti110.pop(2)
7
cti110
[5, 6, 8, 9, 4, 3]
cti110.append(6)
cti110
[5, 6, 8, 9, 4, 3, 6]
cti110.count(6)
2
cti110.remoe(6)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    cti110.remoe(6)
AttributeError: 'list' object has no attribute 'remoe'. Did you mean: 'remove'?
cti110.remove(6)
cti110
[5, 8, 9, 4, 3, 6]
numbers = [4,5,6,7,8,9,1]
numbers
[4, 5, 6, 7, 8, 9, 1]
numTuple = tuple(numbers)
numTuple
(4, 5, 6, 7, 8, 9, 1)
numTuple[1:4]
\
SyntaxError: multiple statements found while compiling a single statement
numTuple [1:4]
(5, 6, 7)
numbers
[4, 5, 6, 7, 8, 9, 1]
numSet = set(numbers)
numSet
{1, 4, 5, 6, 7, 8, 9}
