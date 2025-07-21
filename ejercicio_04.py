#Simulador de facturación con IVA, descuentos y propina
user_price = 1
prices = []
while user_price!= 0:
    user_price = float(input("Ingrese el precio de sus productos o ingrese 0 para salir: "))
    prices.append(user_price)
    total_prices = sum(prices)
user_tip = str(input("Desea agregar una propina? ")).lower()
if user_tip == "si":
    user_tip = int(input("Cuanto quiere dejar (en porcentaje de su compra): "))
    user_tip = user_tip*1/100 * total_prices
elif user_tip == "no":
    print()
custome_card = str(input("Tiene tarjeta de cliente frecuente: ")).lower()
if custome_card == "si":
    custome_card = 0.10*total_prices
elif custome_card == "no":
    print()
iva_prices = 0.12*total_prices
print("Su total se desglosa de la siguiente manera: ")
print("Subtotal:Q", total_prices)
print("Costo por propina:Q", user_tip)
print("Tiene un descuento de Q", custome_card, "por tu tarjeta de usuario frecuente")
print("Cantidad por IVA:Q ", iva_prices)
print("Total:Q", total_prices + user_tip - custome_card + iva_prices)