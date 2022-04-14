# time program

hours = 24
minutes = 60
seconds = 60

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours,":", minutes,":",seconds)

for row in range(1, 4):
    for col in range(row):
    print("*", end="")
print()
