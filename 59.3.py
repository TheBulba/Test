ilosc1 = 0
ilosc2 = 0
ilosc3 = 0
ilosc4 = 0
ilosc5 = 0
ilosc6 = 0
ilosc7 = 0
ilosc8 = 0


print("59.3", file=open('wynik_liczby.txt','a'))
with open("liczby.txt") as file:
    for line in file:

        strn = line.strip()
        strlen = len(strn)
        num = int(strn)

        pow = strlen-1

        i = 1
        ln = 1
        moc = 1
        orginal = num

        if num<10 :
            moc = 1
        else:
            while(i<2):
                while num > 0:
                    jednostka = num // (10**pow)
                    num = num - jednostka * (10**pow)
                    ln = ln * jednostka

                    pow-=1

                if ln < 10:
                    i = 2
                else:
                    num = ln
                    numstr = str(num)
                    ln = 1
                    pow = len(numstr) - 1
                    moc+=1

            if moc == 1:
                ilosc1+=1

                if ilosc1 == 1:
                    najwieksza = orginal
                    najmniejsza = orginal
                elif ilosc1 > 1 and orginal > najwieksza:
                    najwieksza = orginal
                elif ilosc1 > 1 and orginal < najmniejsza:
                    najmniejsza = orginal

            elif moc == 2:
                ilosc2+=1
            elif moc == 3:
               ilosc3+=1
            elif moc == 4:
                ilosc4+=1
            elif moc == 5:
                ilosc5+=1
            elif moc == 6:
                ilosc6+=1
            elif moc == 7:
                ilosc7+=1
            elif moc == 8:
                ilosc8+=1


print("Liczby o mocy 1: ",ilosc1, file=open('wynik_liczby.txt','a'))
print("Liczby o mocy 2: ",ilosc2, file=open('wynik_liczby.txt','a'))
print("Liczby o mocy 3: ",ilosc3, file=open('wynik_liczby.txt','a'))
print("Liczby o mocy 4: ",ilosc4, file=open('wynik_liczby.txt','a'))
print("Liczby o mocy 5: ",ilosc5, file=open('wynik_liczby.txt','a'))
print("Liczby o mocy 6: ",ilosc6, file=open('wynik_liczby.txt','a'))
print("Liczby o mocy 7: ",ilosc7, file=open('wynik_liczby.txt','a'))
print("Liczby o mocy 8: ",ilosc8, file=open('wynik_liczby.txt','a'))
print("Najwieksza liczba o mocy 1 to:", najwieksza, file=open('wynik_liczby.txt','a'))
print("Najmniejsza liczba o mocy 1 to:", najmniejsza, file=open('wynik_liczby.txt','a'))
