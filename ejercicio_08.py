#Calculadora de rumbo entre puntos cardinales
user_coordinate1 = str(input("Ingrese la primera coordenada (norte, sur, este, oeste): ")).lower()
user_coordinate2 = str(input("Ingrese la segunda coordenada (norte, sur, este, oeste): ")).lower()
#Norte
if user_coordinate1 == "norte":
    if user_coordinate2 == "norte":
        print("Continue al norte")
    elif user_coordinate2 == "sur":
        print("Recto hacia al sur")
    elif user_coordinate2 == "oeste":
        print("Noroeste")
    elif user_coordinate2 == "este":
        print("Noreste")
elif user_coordinate1 == "sur":
    if user_coordinate2 == "norte":
        print("Recto hacia al norte")
    elif user_coordinate2 == "sur":
        print("Continue al sur")
    elif user_coordinate2 == "oeste":
        print("Suroeste")
    elif user_coordinate2 == "este":
        print("Sureste")
elif user_coordinate1 == "este":
    if user_coordinate2 == "norte":
        print("Noreste")
    elif user_coordinate2 == "sur":
        print("Sureste")
    elif user_coordinate2 == "oeste":
        print("Recto hacia el oeste")
    elif user_coordinate2 == "este":
        print("Continue al este")
elif user_coordinate1 == "oeste":
    if user_coordinate2 == "norte":
        print("Noroeste")
    elif user_coordinate2 == "sur":
        print("Suroeste")
    elif user_coordinate2 == "oeste":
        print("Continue al oeste")
    elif user_coordinate2 == "este":
        print("Recto hacia el este")
else:
    print("Error, vuelva a intentar")