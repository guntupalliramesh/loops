no = int(input("Enter a number :"))
factor = 1
if no<=0:
    print("no factorial")
else:
    for x in range(1,no+1):
        factor=factor*x
print("the factorial of ",no,"is",factor)