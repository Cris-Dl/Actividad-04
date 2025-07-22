#Simulador de entradas al cine con validación multiple
user_age = int(input("Ingrese su edad: "))
week_day = str(input("Ingrese dia de la semana: ")).lower()
student_user = str(input("Eres estudiante? ")).lower()
print()
if student_user == "si":
    if week_day == "miercoles":
        if user_age >= 13:
            print("Información de su recibo")
            print("Hoy hay entradas 2 x 1, que disfrute")
            print("Total: Q35.00")
        elif user_age < 13:
            print("Información de su recibo")
            print("Hoy hay entradas 2 x 1, que disfrute")
            print("Total: Q35.00")
            print("IMPORTANTE. Eres menor de 13 años, no puedes ver peliculas para mayores de 15 años, solo apto para todo público")
        else:
            print("Error, vuelva a intentar")
    elif week_day != "miercoles":
        if user_age >= 13:
            print("Información de su recibo")
            print("Total: Q35.00")
        elif user_age < 13:
            print("Información de su recibo")
            print("Total: Q35.00")
            print("IMPORTANTE. Eres menor de 13 años, no puedes ver peliculas para mayores de 15 años, solo apto para todo público")
    else:
        print("Error, vuelva a intentar")
elif student_user == "no":
    if week_day == "miercoles":
        if user_age >= 13:
            print("Información de su recibo")
            print("Hoy hay entradas 2 x 1, que disfrute")
            print("Total: Q50.00")
        elif user_age < 13:
            print("Información de su recibo")
            print("Hoy hay entradas 2 x 1, que disfrute")
            print("Total: Q50.00")
            print("IMPORTANTE. Eres menor de 13 años, no puedes ver peliculas para mayores de 15 años, solo apto para todo público")
        else:
            print("Error, vuelva a intentar")
    elif week_day != "miercoles":
        if user_age >= 13:
            print("Información de su recibo")
            print("Total: Q50.00")
        elif user_age < 13:
            print("Información de su recibo")
            print("Total: Q50.00")
            print("IMPORTANTE. Eres menor de 13 años, no puedes ver peliculas para mayores de 15 años, solo apto para todo público")
    else:
        print("Error, vuelva a intentar")
else:
    print("Error, vuelve a intentar")