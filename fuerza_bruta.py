from string import ascii_lowercase
import getpass

def fuerza_bruta(password):
    intentos = 0
    encontrado = ''

    for letra in password:
        for posible in ascii_lowercase:
            intentos += 1
            if posible == letra:
                encontrado += posible
                break

    return intentos


password = getpass.getpass("Ingrese la contraseña: ").lower()  # Oculta la entrada y convierte a minúsculas
intentos = fuerza_bruta(password)
print(f"La contraseña fue forzada en {intentos} intentos")