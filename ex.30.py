no = int(input("Enter a 4 digit no:"))
sum = 0
while no != 0:
    r = no%10
    no = no//10
    sum += r
print("the sum of 4 digit's no:",sum)