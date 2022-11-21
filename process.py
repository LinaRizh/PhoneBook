from ui import *
from phone_import import *
from phone_export import *

def phone_book():
    m = mode()
    d = data()
    if  m == 0:
        format_inp(d)
    elif m == 1:
        n = mode_exp()
        if n==0 or n==1:
            format_exp(d,n)
        else: print('Вы ввели выбрали несуществующий фомат представления данных, работа со справочником прекращена')
    else: 
        print('Вы ввели несуществующий режим работы, работа со справочником прекращена')



