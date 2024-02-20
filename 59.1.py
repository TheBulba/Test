print("59.1", file=open('wynik_liczby.txt','a'))
print(" ", file=open('wynik_liczby.txt','a'))
with open("liczby.txt") as file:
    for line in file:
        strn = line.strip()
        num = int(strn)
        div = 2
        sum = 0
        pot = 0

        if num > 1:
            print(num, end=": ", file=open('wynik_liczby.txt','a'))
            while(num>1):
                if num%div == 0:
                    num = num/div
                    print (div, end=" ", file=open('wynik_liczby.txt','a'))

                    if div%2!=0:
                        if div!=pot:
                            sum=sum+1
                            pot=div

                else:
                    div=div+1

            if sum==3:
                print(" Tak", file=open('wynik_liczby.txt','a'))
            else:
                print(" Nie", file=open('wynik_liczby.txt','a'))
        else:
            print (1, file=open('wynik_liczby.txt','a'))

 print ("", file=open('wynik_liczby.txt','a'))
