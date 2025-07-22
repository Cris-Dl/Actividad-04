#Comparador de fechas (tipo digital)
user1_day1 = int(input("Ingrese el numero de día de la primera fecha: "))
user1_month1 = int(input("Ingrese el numero de mes de la primera fecha: "))
user1_year1 = int(input("Ingrese el numero de año de la primera fecha: "))

user2_day2 = int(input("Ingrese el numero de día de la segunda fecha: "))
user2_month2 = int(input("Ingrese el numero de mes de la segunda fecha: "))
user2_year2 = int(input("Ingrese el numero de año de la segunda fecha: "))

if user1_year1 == user2_year2:
    if user1_month1 == user2_month2:
        if user1_day1 > user2_day2:
            print("La primera fecha es mayor que la segunda")
        elif user2_day2 > user1_day1:
            print("La segunda fecha es mayor que la segunda")
        elif user1_day1 == user2_day2:
            print("Ni una fecha es mayor que otra")
        else:
            print("Error, vuelva a intentar")
    elif user1_month1 > user2_month2:
        print("La primera fecha es mayor que la segunda fecha")
    elif user2_month2 > user1_month1:
        print("La segunda fecha es mayor que la primera")
    else:
        print("Error, vuelva a intentar")
elif user1_year1 > user2_year2:
    print("La primera fecha es mayor que la segunda fecha")
elif user2_year2 > user1_year1:
    print("La segunda fecha es mayor que la primera")
else:
    print("Error, vuelva a intentar")

if user1_month1 == user2_month2 and user1_year1 == user2_year2:
    print("Las dos fechas se encuentran en el mismo mes y año")
elif user1_year1 != user2_year2 or user1_month1 != user2_month2:
    print("No se encuentran en el mismo mes o año")

if user1_day1 >0 and user2_day2 > 0:
    if user1_day1 > user2_day2:
        print("La diferencia de dias es de:", user1_day1 - user2_day2)
    elif user2_day2 > user1_day1:
        print("La diferencia de dias es de:", user2_day2 - user1_day1)
    elif user1_day1 == user2_day2:
        print("No hay diferencia de dias")
    else:
        print("Error, vuelva a intentar")