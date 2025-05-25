#1)დაწერე პროგრამა, რომელიც while ციკლით დაბეჭდავს რიცხვებს 1-დან 10-მდე.2)დაწერე პროგრამა, რომელიც დაბეჭდავს რიცხვებს 10-დან 1-მდე.3)კომენტარებით ახსენი while loop. 4)დაწერე პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. სწორი პაროლია "python123". სანამ სწორად არ შეიყვანს, მოთხოვე თავიდან.5)მომხმარებელმა უნდა შეიყვანოს რიცხვი n. პროგრამამ while ციკლით უნდა დაითვალოს 1-დან n-მდე რიცხვების ჯამი.

num = 1
while num < 10:
    print(num)
    num += 1


num = 10
while num > 0:
    print(num)
    num -= 1

#არის ციკლი Python-ში, რომელიც ასრულებს კოდის ბლოკს მანამ, სანამ პირობა მართალია 

user_password = input("enter password: ")
correct_password = "python123"
while user_password != correct_password:
    print('try again')
    user_password = input("enter password: ")
print("correct")






n = int(input("enter number n: "))
i = 1
summ = 0

while i <= n:
    summ += i
    i += 1

print("sum:", summ)