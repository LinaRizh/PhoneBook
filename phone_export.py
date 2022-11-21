
def format_exp(l, m):
    if int(m) == 0:
        with open('phone_book_1.txt','r') as file:
            f = file.readlines()
            for line in f:
                d = line.split(',')
                if d[0]==l:
                    print(*d[0:4], end="\n")
    elif int(m) == 1:
        with open('phone_book_2.txt',encoding='UTF-8') as file:
            f = file.readlines()
            for i in range(len(f)):
                if f[i].strip()==l:
                    print(*f[i:i+4], end="\n")