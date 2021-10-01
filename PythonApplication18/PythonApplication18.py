def login_user():
    print('\t\t\tВход в программу\n')
    password = "code"
    password_useer = input("Введите код: \n")
    attempt = 1
    while password_useer != password:                                  
        print("Вы попыталсь вести пароль", attempt, "раз\n")
        guess = input("Введите паролль заново: \n")                       
        attempt += 1
        if (attempt == 5):
            print('Вы пытались зайти слишком часто, повторите попытку через некоторое время\n')
            break;
        else:
            print("Вы вошли в учетную запись\n")
            break;

def factorial():
    print('\t\t\tФакториал\n')
    num = int(input('Введите число - \n'))
    factor = 0
    if num > 0: 
        factor = 1
        for i in range(2,num + 1):
            factor = factor * i
        print (factor)
    else:
        print('Ошибка вы ввели число 0 или меньше 0, повторите попытку\n')


def maximum():
    print('\t\t\tНахождение максимального числа - \n')
    num1 = int(input('Введите число - '))
    max = num1%10
    num1 = num1//10
    while num1 > 0:
        if num1%10 > max:
            max = num1%10
        num1 = num1//10
    print("Максимальная цифра в ряде - ", max,"\n")

login_user()
factorial()
maximum()