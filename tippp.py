
# TIP CALCULATOR

keep_going = "y"

while keep_going == "y" or keep_going "Y":
    # price of food
    pre_tip = float(input("Enter Price of Food: "))

    # calculate 18% tip (price * .18)


    tip = float(input("How much to tip? (.15, .20) "))

    if tip == .15:

    tipPer = pre_tip * 0.15

    elif tip == .20:
        tipPer = pre_tip * 0.20

        else:
            print ("Invalicd entry!")
            print("20% tip will be applied")

    # calculate total price , add the above

    total = pre_tip + tipPer

    print("total is $", total, sep="")

    keep_going = input("\ndo you want to calculate another tip? (y/n): ")
