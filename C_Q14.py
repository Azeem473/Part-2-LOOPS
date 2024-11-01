num = int(input("Enter any number: "))

for i in range(0,10):
    if num >=i:
        print("break the statment")
        break
    elif num <=i:
        print(num,"is smaller")
    else:
        print(num,"is equal")