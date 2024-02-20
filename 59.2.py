print("59.2", file=open('wynik_liczby.txt','a'))
print ("Liczba:            Liczba odwrócona:       Suma:           Czy jest palindromem:", file=open('wynik_liczby.txt','a'))

with open("liczby.txt") as file:
    for line in file:
        print("", file=open('wynik_liczby.txt','a'))
        strn = line.strip()
        strlen = len(strn)
        num = int(strn)
        pr = 18 - strlen
        rev = 0

        print (num, end=":", file=open('wynik_liczby.txt','a'))

        #rowne odstepy
        i = 0
        while i < pr:
            print(end=" ", file=open('wynik_liczby.txt','a'))
            i+=1

        od = num
        #odwracanie
        while od!=0 :
            rev = rev * 10 + (od%10)
            od //= 10

        print (rev, end="", file=open('wynik_liczby.txt','a'))
        rs = str(rev)

        #rowne odstepy
        i = 0
        pr = 24 - len(rs)
        while i < pr:
            print(end=" ", file=open('wynik_liczby.txt','a'))
            i+=1

        #suma
        suma = num + rev
        print(suma, end="", file=open('wynik_liczby.txt','a'))
        sos = str(suma)
        #rowne odstepy
        i = 0
        pr = 24 - len(sos)
        while i < pr:
            print(end=" ", file=open('wynik_liczby.txt','a'))
            i+=1

        #odwrocona suma
        os = suma
        ros = 0
        while os!=0:
            ros = ros * 10 + (os%10)
            os //= 10

        if suma == ros:
            print (" tak", end="", file=open('wynik_liczby.txt','a'))

        else:
            print(" nie", end="", file=open('wynik_liczby.txt','a'))
