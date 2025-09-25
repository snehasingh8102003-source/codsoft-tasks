def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if(b!=0):
        return a/b
    else:
        return("division can't be possible")
def calculator():
    while True:
        print("1.add")
        print("2.subtract")
        print("3.multiply")
        print("4.divide")
        print("5. exit")
        num=input("enter choice b/w 1 to 5")
        if(num==5):
            print("not possible")
            break
        if(num in "1","2","3","4"):
            num1=int(input("enter no1. "))
            num2=int(input("enter no2. "))
            if(num=="1"):
                print(add(num1,num2))
            elif(num=="2"):
                print(subtract(num1,num2))
            elif(num=="3"):
                print(multiply(num1,num2))
            elif(num=="4"):
                print(divide(num1,num2))
        else:
                print("error")
calculator()