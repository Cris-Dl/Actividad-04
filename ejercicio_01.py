#Simulador de votación con validación cruzada
name_person = str(input("Ingrese su nombre completo: "))
dpi_person = int(input("Ingrese su DPI: "))
departamento_person = str(input("Ingrese su departamento: ")).lower()
year_birth = int(input("Ingrese su año de nacimiento: "))
numbers_letters = len(name_person)
numbers_dpi = len(str(dpi_person))
if numbers_letters < 5:
    print("Tu nombre tiene menos de 5 letras, no puede votar")
elif numbers_dpi < 13 or numbers_letters > 13:
    print("Error de DPI, no puede votar")
elif departamento_person == "petén"  and year_birth == 2008 or departamento_person == "alta verapaz" and year_birth == 2008:
    print("Ya que eres de", departamento_person, " puedes votar")
    print("Bienvenido", name_person, ", su centro de votación está en", departamento_person)
elif year_birth > 2007:
    print("Eres menor de 18 años, no puedes votar")
elif numbers_letters < 5:
    print("Tu nombre tiene menos de 5 letras, no puede votar")
elif numbers_dpi < 13 or numbers_letters > 13:
    print("Error de DPI, no puede votar")
else:
    print("Bienvenido", name_person, ", su centro de votación está en", departamento_person)