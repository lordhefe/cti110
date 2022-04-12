# calculate profits for week *define days of week

# ask user how many days business operates
## initilize running total

# start for loop (ask for profit for each day)
# add profit to totalRevenue
# notify user of totalRevenue generated

days = int(input("Enter number of days your business operates: "))

# initilize accumulator variable

totalRevenue = 0
for day in range(1, days+1):
    print ("Enter profit for day", day,end=": ")
    profit = float(input())

    totalRevenue = totalRevenue + profit
    #or
     #totalRevenue = totalRevenue + profit

    
