
numb = int(input('Введите номер месяца: '))
days = (31,28,31,30,31,30,31,31,30,31,30,31)


if int(numb) <1 or int(numb) >12:
    print('Такого месяца нет!')
else:
    print(days[numb-1])