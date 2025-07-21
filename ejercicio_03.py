#Sistema de autenticación avanzado con penalización
user_list = {"Juan Jose":"admin123", "Jorge Tello":"12345", "Santiago Batz":"123456"}
user_attempt = str(input("Ingrese su usuario: "))
if user_attempt in user_list:
    user_password = input("Ingrese su contraseña: ")
    if user_password == user_list[user_attempt]:
        print("Bienvenido",user_attempt)
        print("1- Ver perfil")
        print("2- Cambiar contraseña")
        print("3- Cerrar sesión")
    else:
        print("Repita nuevamente")
        user_password = input("Ingrese su contraseña: ")
        if user_password == user_list[user_attempt]:
            print("Bienvenido", user_attempt)
            print("1- Ver perfil")
            print("2- Cambiar contraseña")
            print("3- Cerrar sesión")
        else:
            print("Repita nuevamente")
            user_password = input("Ingrese su contraseña: ")
            if user_password == user_list[user_attempt]:
                print("Bienvenido", user_attempt)
                print("1- Ver perfil")
                print("2- Cambiar contraseña")
                print("3- Cerrar sesión")
            else:
                print("ACCESO BLOQUEADO")
else:
    print("Usuario incorrecto")