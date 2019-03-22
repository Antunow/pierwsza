import tkinter,sys
from tkinter import messagebox
def lpierwsze(do):
    pierwsze=[]
    for i in range(1,int (do)):
        dzielniki = []
        for j in range(2,i+1):
            if i%j==0 :
                dzielniki.append(j)
        if len(dzielniki)==1:
            pierwsze.append(i)
    return pierwsze



def maxdziel(liczba):
    wynik = {0: 0}
    iledziel = 0
    for i in range(1,int (liczba+1)):
        dzielniki = []

        for j in range(1,i+1):
            if i%j==0 :
                dzielniki.append(j)
        if len(dzielniki)>iledziel:
            iledziel=len(dzielniki)
            wynik={i:iledziel}
        print("pracujęnad liczbą", i)
    print(wynik,'\n',dzielniki)



def napierwsze(dana):
    pierwsze = []
    dpierw=[]
    liczba = dana
    for i in range(1, int(liczba)):
        dzielniki = []

        for j in range(2, i + 1):
            if i % j == 0:
                dzielniki.append(j)
        if len(dzielniki) == 1:
            pierwsze.append(i)

    while liczba!=1:        #
        for i in pierwsze:

            if liczba%i==0:
                dpierw.append(i)
                liczba=liczba/i

    print (dana, dpierw,liczba )

def skrpierw():
    global licznik_bledu1, licznik_bledu

    stopien=e1.get()
    liczba = e2.get()
    sprawdzenie="1234567890"
    for i in range(0,len(stopien)):
        if stopien[i] not in sprawdzenie:
            licznik_bledu+=1
            e1.delete(0, 100)
            if licznik_bledu <= 3:
                messagebox.showinfo("NIE KOMBINUJ",
                                    "Te uważaj sobie bo spotka cie zasłużona kara !!!\n Wykładnik musi być liczbą ")
    for i in range(0, len(liczba)):
        if liczba[i] not in sprawdzenie:
            licznik_bledu1+= 1
            e2.delete(0, 100)
            if licznik_bledu <= 3 or licznik_bledu1 <=3:
                messagebox.showinfo("NIE KOMBINUJ",
                                    "Te uważaj sobie bo spotka cie zasłużona kara !!!\n podstawa musi być liczbą ")

    if licznik_bledu==4 or licznik_bledu1==4:
         messagebox.showinfo("OSTRZEGAM CIĘ","nie kombinuj!!!\n sroga kara sie zbliża !!! ")
    if licznik_bledu==5 or licznik_bledu==5:
        for i in range(0,10):
            messagebox.showinfo("No i musisz kombinować","Teraz cierp\n i pamietaj że wiem gdzie mieszkasz !!!\n nawiedzę cie w nocy i wymierze resztę kary")
        messagebox.showinfo("masz już dosyć ",
                            "Mam nadzieję żę masz już dosyć\n nastepnym razem bedzie mniej przyjemnie")
    if licznik_bledu==7 or licznik_bledu1==7:
        for i in range(0,50):
            messagebox.showinfo("Apokalipsa","ostrzegałęm wielokrotnie\n nocna kara będzie dotliwa!!!")
        messagebox.showinfo("Przesadziłaś ", "Jesteś niereformowalna!!!\nNie bedę z tobą współpracował", )
        sys.exit()

    stopien=int(stopien)
    liczba=int(liczba)

    pierwsze=lpierwsze(liczba+1)
   # print ('wyznaczyłęm liczby pierwsze',pierwsze)

    zmienna= liczba
    dzielniki=[]
    przedpierw=[]
    podstawa=[]
    iloczyn1=1
    iloczyn2=1
    if liczba in pierwsze:
        print ("pierwiastek ",stopien,"z ",liczba,'niedaje sie skrócić')

    while zmienna!=1:                   # wyznazca dzielniki
         for i in pierwsze:
             if zmienna%i==0:
                dzielniki.append(i)
                zmienna=zmienna/i

    #print ("wyznaczyłem dzielniki",dzielniki)
    dzielniki.sort()
    pupa=dzielniki.copy()

    for ii in dzielniki:                  #szuka co można wyciągnąć przed pierwiastek
        licznik=0

        for j in pupa:
            if ii ==j:
                licznik+=1              #todo problem z usywaniem elemetów chce usówać jeden wiecej niż się w nim znajduje są dwie petle mozę trrzba stwożyć roboczą listę ?
        if licznik >=stopien:
            przedpierw.append(ii)

            for xy in range(0,stopien):
                pupa.pop(0)



        elif licznik<stopien and licznik!=0 :
            #for z in range(0,licznik):
                podstawa.append(ii)
                pupa.pop(0)
    for i in przedpierw:
        iloczyn1=iloczyn1*i
    for i in podstawa:
        iloczyn2=iloczyn2*i



   # wynik="pierwiastek ",stopien," stopnia z ",liczba,"można skrócić do formy",iloczyn1,"pierwiastków",stopien,"stopnia z ",iloczyn2
    l4.config(text=("pierwiastek "+str(stopien)+" stopnia z "+str(liczba)+"można skrócić do formy\n"+str(iloczyn1)+" pierwiastków "+str(stopien)+" stopnia z "+str(iloczyn2)))
    l5.config(text="Skracany pierwiastek\npierwiastek "+str(stopien)+" stopnia z "+str(liczba))
stopien=1
liczba=1
licznik_bledu=0
licznik_bledu1=0

okno=tkinter.Tk()
l1=tkinter.Label(okno,text="Skracanie pierwiastków", bg="red")
l2=tkinter.Label(okno,text="podaj stopień pierwiaska")
l3=tkinter.Label(okno,text="podaj liczbę do spierwaistkowania")
l4=tkinter.Label(okno,text="wynik")
l5=tkinter.Label(okno,text="skracany pierwiastek")
#l6=tkinter.Label(okno,text="wynik")

e1=tkinter.Entry(okno,text="wpisz stopień")
e2=tkinter.Entry(okno,text="wpisz liczbę do spierwiastkowania")



b1=tkinter.Button(okno,text="skróć pierwiastek",bg="blue",fg="yellow",command=skrpierw)

l1.grid(columnspan=3)
l2.grid(row=1)
l3.grid(row=2)
l4.grid(row=3,column=1)
l5.grid(row=2,column=2 )


e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
b1.grid(row=3)




okno.mainloop()
