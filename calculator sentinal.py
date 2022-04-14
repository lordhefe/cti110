# price of food
# -1 is sentinal
pre_tip = float(input("Enter Price of Food or -1 to terminate: "))

while pre_tip != -1:

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

    

    pre_tip = float(input("Enter Price of Food or -1 to terminate: "))
