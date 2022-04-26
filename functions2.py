def main():

    hours, rate = get_input()

    calc_gross(hours, rate)
    
    print("bye")


def get_input():
    
    hours = float( input("Enter hours worked: "))
    
    rate = float( input("Enter pay rate: "))

    return hours, rate


def calc_gross(h,r):

    grossPay = h * r

    print("gross pay is $", grossPay, sep="")


main()
