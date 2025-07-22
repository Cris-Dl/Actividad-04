#Verificador de fecha válida con día de la semana
user_day = int(input("Ingrese el numero de día: "))
user_month = int(input("Ingrese el numero del mes: "))
user_year = int(input("Ingrese el numero del año: "))

if user_year%4 == 0 and user_month == 2 and user_day < 30 and user_day > 0:
    print("Fecha valida")
if user_month == 3 or user_month == 1 or user_month == 5 or user_month == 7 or user_month == 8 or user_month == 10 or user_month == 12:
    if user_day <32 and user_day>0:
        print("Fecha valida")
    else:
        print("Fecha invalida")
elif user_month == 4 or user_month == 6 or user_month == 9 or user_month == 11:
    if user_day < 31 and user_day > 0:
        print("Fecha valida")
    else:
        print("Fecha invalida")
elif user_month == 2:
    if user_day > 0 and user_day < 29:
        print("Fecha valida")
    else:
        print("Fecha invalida")
else:
    print("Error, vuelva a intentar")

if user_month <= 2:
    user_month = user_month + 12
    user_year = user_year -1
else:
    user_month = user_month -2
a = user_year%100
b = user_year/100
d = (700 + (user_month*26-2)/10+user_day+a+a/4+b/4-b*2)%7

if round(d) -1 == 0:
    print("Segun la fecha, el dia cae un domingo")
elif round(d) -1 == 1:
    print("Segun la fecha, el dia cae un lunes")
elif round(d) -1 == 2:
    print("Segun la fecha, el dia cae un martes")
elif round(d) -1 == 3:
    print("Segun la fecha, el dia cae un miercoles")
elif round(d) -1 == 4:
    print("Segun la fecha, el dia cae un jueves")
elif round(d) -1 == 5:
    print("Segun la fecha, el dia cae un viernes")
elif round(d) -1 == 6:
    print("Segun la fecha, el dia cae un sabado")