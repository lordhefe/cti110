keep_going = "y"

while keep_going == "y" or keep_going "Y":
    
    score = float (input("Enter score Please:") )

    while score >100 or score <0 :
        print("\nInvalid Score Entered!!")
        print("Must be between 0 and 100")

        score = float(input("enter score again: "))

    if score >=90:
        print("A")
    else:
        if score >=80:
        print(B")
        else:
             if score >=70:
             print("C")
            else:
                 if score >=60:
             print("D")
                else:
                     if score <60:
                         print("F")
             
    keep_going = input("\ndo you want to enter another score? (y/n): ")
