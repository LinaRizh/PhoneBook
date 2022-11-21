import os

def format_inp(l):
    with open('phone_book_1.txt', 'a') as file:
        if (os.stat("phone_book_1.txt").st_size == 0)==False:
            file.write('\n')
        file.write((',').join(l.split(',')))
        file.write('\n')
    with open('phone_book_2.txt', 'a') as file:
        if (os.stat("phone_book_2.txt").st_size == 0)==False:
            file.write('\n')
        file.write(('\n'.join(l.split(','))))
        file.write('\n') 
