def mode():
    return int(input('Выберите режим работы со справочником: 0 - импорт, 1 - экспорт: '))
   
def data():
    return input('Введите данные для импорта через запятую (фамилия,имя,телефон,описание) или фамилию для экспорта: ')

def mode_exp():
    print('Выберите формат представления данных')
    print('\n0\nфамилия,имя,телефон,описание')
    print('\n1\nфамилия\nимя\nтелефон\nописание\n')
    return(int(input()))
   

def export (l):
    print(l)