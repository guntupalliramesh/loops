number = int(input("Enter a number: "))
if number > 1:
    for x in range(2, number):
        if (number % x) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")