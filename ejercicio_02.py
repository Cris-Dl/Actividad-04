#Calculadora de impuestos progresivos + deducciones
annual_income = int(input("Escriba su ingreso anual: "))
number_dependents = int(input("Escriba la cantidad de dependientes: "))
if annual_income < 40000 and number_dependents > 2:
    print("Usted no debe pagar impuestos")
elif annual_income >= 0 and annual_income <= 30000:
    print("Cantidad por impuestos: ", annual_income*0.05)
    print("Cantidad por dependientes: ", number_dependents*1000)
    print("Total: ", annual_income * 0.05 + number_dependents*1000)
elif annual_income >= 30001 and annual_income <= 60000:
    print("Cantidad por impuestos: ", annual_income*0.10)
    print("Cantidad por dependientes: ", number_dependents*1000)
    print("Total: ", annual_income * 0.10 + number_dependents*1000)
elif annual_income >= 60001 and annual_income <= 100000:
    print("Cantidad por impuestos: ", annual_income*0.15)
    print("Cantidad por dependientes: ", number_dependents*1000)
    print("Total: ", annual_income * 0.15 + number_dependents*1000)
elif annual_income >= 100000:
    print("Cantidad por impuestos: ", annual_income*0.20)
    print("Cantidad por dependientes: ", number_dependents*1000)
    print("Total: ", annual_income * 0.20 + number_dependents*1000)
else:
    print("Error vuelva a intentar")