#Clasificador de envio con múltiples condiciones
package_weight = float(input("Ingrese el peso del paquete (en kg): "))
package_distance = float(input("Ingrese la distancia que recorrera el paquete (en km): "))
urgent_package = str(input("Es urgente entregar el paquete? ")).lower()
package_size = str(input("Escriba si es pequeño/mediano/grande el paquete: ")).lower()
total_price=0
if package_weight > 0 and package_weight < 5 and urgent_package == "no":
    if package_distance > 0 and package_size <= 10:
        print("Su recibo se desglosa de la siguiente manera:")
        print("Ya que pesa menos de 5kg y no es un paquete urgente se le descontará Q20.00")
        print("Total:Q", 50-20)
    elif package_distance > 10 and package_weight < 50:
        print("Su recibo se desglosa de la siguiente manera:")
        print("Ya que pesa menos de 5kg y no es un paquete urgente se le descontará Q20.00")
        print("Total:Q", 100 - 20)
    elif package_distance > 50:
        print("Su recibo se desglosa de la siguiente manera:")
        print("Ya que pesa menos de 5kg y no es un paquete urgente se le descontará Q20.00")
        print("Total:Q", 175 - 20)
    else:
        print("Error, vuelva a intentar")
elif package_weight > 0 and package_weight <5:
    if package_distance > 0 and package_distance <=10:
        if package_size == "pequeño":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q10")
                print("Total:Q110")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q10")
                print("Total:Q60")
            else:
                print("Error, vueva a intentar")
        elif package_size == "mediano":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q20")
                print("Total:Q120")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q20")
                print("Total:Q70")
            else:
                print("Error, vueva a intentar")
        elif package_size == "grande":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q30")
                print("Total:Q130")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q30")
                print("Total:Q80")
            else:
                print("Error, vueva a intentar")
    if package_distance > 10 and package_distance < 50:
        if package_size == "pequeño":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q10")
                print("Total:Q160")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q10")
                print("Total:Q110")
            else:
                print("Error, vueva a intentar")
        elif package_size == "mediano":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q20")
                print("Total:Q170")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q20")
                print("Total:Q120")
            else:
                print("Error, vueva a intentar")
        elif package_size == "grande":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q30")
                print("Total:Q180")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q30")
                print("Total:Q130")
            else:
                print("Error, vueva a intentar")
    elif package_distance > 50:
        if package_size == "pequeño":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q10")
                print("Total:Q235")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q10")
                print("Total:Q185")
            else:
                print("Error, vueva a intentar")
        elif package_size == "mediano":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q20")
                print("Total:Q245")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q20")
                print("Total:Q195")
            else:
                print("Error, vueva a intentar")
        elif package_size == "grande":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q30")
                print("Total:Q255")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q30")
                print("Total:Q205")
            else:
                print("Error, vueva a intentar")
elif package_weight > 5 and package_weight <20:
    if package_distance > 0 and package_distance <=10:
        if package_size == "pequeño":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q10")
                print("Total:Q130")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q10")
                print("Total:Q80")
            else:
                print("Error, vueva a intentar")
        elif package_size == "mediano":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q20")
                print("Total:Q140")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q20")
                print("Total:Q90")
            else:
                print("Error, vueva a intentar")
        elif package_size == "grande":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q30")
                print("Total:Q150")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q30")
                print("Total:Q100")
            else:
                print("Error, vueva a intentar")
    if package_distance > 10 and package_distance < 50:
        if package_size == "pequeño":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q10")
                print("Total:Q180")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q10")
                print("Total:Q130")
            else:
                print("Error, vueva a intentar")
        elif package_size == "mediano":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q20")
                print("Total:Q190")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q20")
                print("Total:Q140")
            else:
                print("Error, vueva a intentar")
        elif package_size == "grande":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q30")
                print("Total:Q200")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q30")
                print("Total:Q150")
            else:
                print("Error, vueva a intentar")
    elif package_distance > 50:
        if package_size == "pequeño":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q10")
                print("Total:Q255")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q10")
                print("Total:Q205")
            else:
                print("Error, vueva a intentar")
        elif package_size == "mediano":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q20")
                print("Total:Q265")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q20")
                print("Total:Q215")
            else:
                print("Error, vueva a intentar")
        elif package_size == "grande":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q30")
                print("Total:Q275")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q30")
                print("Total:Q225")
            else:
                print("Error, vueva a intentar")
elif package_weight > 20:
    if package_distance > 0 and package_distance <=10:
        if package_size == "pequeño":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q10")
                print("Total:Q160")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q10")
                print("Total:Q110")
            else:
                print("Error, vueva a intentar")
        elif package_size == "mediano":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q20")
                print("Total:Q170")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q20")
                print("Total:Q120")
            else:
                print("Error, vueva a intentar")
        elif package_size == "grande":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q30")
                print("Total:Q180")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q30")
                print("Total:Q130")
            else:
                print("Error, vueva a intentar")
    if package_distance > 10 and package_distance < 50:
        if package_size == "pequeño":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q10")
                print("Total:Q210")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q10")
                print("Total:Q160")
            else:
                print("Error, vueva a intentar")
        elif package_size == "mediano":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q20")
                print("Total:Q220")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q20")
                print("Total:Q170")
            else:
                print("Error, vueva a intentar")
        elif package_size == "grande":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q30")
                print("Total:Q230")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q30")
                print("Total:Q180")
            else:
                print("Error, vueva a intentar")
    elif package_distance > 50:
        if package_size == "pequeño":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q10")
                print("Total:Q285")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q10")
                print("Total:Q235")
            else:
                print("Error, vueva a intentar")
        elif package_size == "mediano":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q20")
                print("Total:Q295")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q20")
                print("Total:Q245")
            else:
                print("Error, vueva a intentar")
        elif package_size == "grande":
            if urgent_package == "si":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q50")
                print("Cargo por tamaño:Q30")
                print("Total:Q305")
            elif urgent_package == "no":
                print("Su recibo se desglosa de la siguiente manera:")
                print("Cargo por urgencia:Q0")
                print("Cargo por tamaño:Q30")
                print("Total:Q255")
            else:
                print("Error, vueva a intentar")
else:
    print("Error, vuelva a intentar")
