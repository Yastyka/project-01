def switch_it_up(number):
    name_numb = {
        '0' : 'Zero', 
        '1' : 'One', 
        '2' : 'Two', 
        '3' : 'Three', 
        '4' : 'Four', 
        '5' : 'Five', 
        '6' : 'Six', 
        '7' : 'Seven', 
        '8' : 'Eight', 
        '9' : 'Nine'
}
    for n in number:
        print(name_numb[n] , end = ' ')


number = input('Введи число: ')
switch_it_up(number)
