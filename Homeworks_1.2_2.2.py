frst_qrt = (1, 2, 3)
sec_qrt = (4, 5, 6)
thrd_qrt = (7, 8, 9)
frth_qrt = (10, 11, 12)

month = int(input("Введите номер месяца: "))

def quarter_of(month):
    if month in frst_qrt:
      return "Месяц является частью первого квартала"
    elif month in sec_qrt:
        return "Месяц является частью второго квартала"
    elif month in thrd_qrt:
       return "Месяц является частью третьего квартала"
    elif month in frth_qrt:
       return "Месяц является частью четвертого квартала"
    else:
       return "Ошибка"
print(quarter_of(month))


