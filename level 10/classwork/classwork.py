num1 = input("enter number: ")
num2 = input("enter number: ")

if num1 > num2:
    print(num1)
else:
    print(num2)


num3 = input("enter number: ")
num4 = input("enter number: ")

if num3 < num4:
    print("მეტია")
else:
    print("ნაკლებია")



for i in range(1, 101):
    if i % 2 == 0:
        print(f"{i} ლუწია")
    else:
        print(f"{i} კენტია")



number = int(input("enter number: "))

if number % 2 == 0:
    print(f"{number} ლუწია")
else:
    print(f"{number} კენტია")
