
#zad1

def func1 (litera, nazwisko):
    return litera + '.' + nazwisko

print(func1('K' , 'Iwon'))

#zad2


def func2(imie,nazwisko):

    return imie[0].upper() + "." + nazwisko[0].upper() + nazwisko[1:]

print(func2('kamila' , 'iwon'))

#zad3
def func3(dwiepierwsze, dwieostatnie, wiek):
    rok = dwiepierwsze * 100 + dwieostatnie
    return rok - wiek

print(func3(20,22,23))

#zad4
def func4(imie,nazwisko,funkcja):
    return funkcja(imie,nazwisko)

print(func4('kamila' , 'iwon', func2))

#zad5

def func5 (liczba1, liczba2):
    if(liczba1>0 and liczba2>0 and liczba2 != 0):
        return liczba1/liczba2
    return 0

print(func5(5,7))

#zad6


suma = 0
while suma < 100 :
    a = int(input("podaj liczbe"))
    suma += a

print(suma)

#zad7

def func7(lista):
    return tuple(lista)

print(func7([3,4,5]))

#zad8

b = int(input("podaj długośc listy"))
lista8 = []
for x in range (0,b):
    liczba = int(input("podaj liczbe"))
    lista8.append(liczba)

lista8 = tuple(lista8)
print(lista8)

#zad9

def func9 (liczba):
    tydzien = ["poniedziałek","wtorek","środa","czwartek","piatek", "sobota", "niedziela"]
    return tydzien[liczba-1]

print(func9(7))

#zad10
def func10(tekst):
    if tekst[::-1] == tekst :
        return True
    return False


print(func10('kamila'))
print(func10('kajak'))