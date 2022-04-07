
##salary = float (input("Enter Salary Please:") )
##
##years = float (input("Enter years on job Please:") )
##
### Evaluate Salary
##
##if salary >= 30000:
##    if years >= 2:
##
##        print("you Get The Loan!")
##        else:
##
##            print("you dont get the loan")
##            print("you haven't worked for 2 or more years")
##
##else:
##    
##            print("you dont qualify")
##            print("you dont make enough")

if salary >= 30000 and years >= 2:

    print("you qualify")
else:

    print("you dont qualify")

    if salary >= 30000 or years >= 2:

    print("you qualify")
else:

    print("you dont qualify")
