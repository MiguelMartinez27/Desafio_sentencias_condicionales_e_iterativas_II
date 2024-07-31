def obtener_respuesta_si_no(pregunta):
    while True:
        respuesta = input(pregunta + " (si/no): ").lower()
        if respuesta in ["si", "no"]:
            return respuesta == "si"
        print("Por favor, responda solo 'si' o 'no'.")

def primeros_auxilios():
    print("Bienvenido al sistema de guía de primeros auxilios.")
    
    if responde_a_estimulos():
        valorar_necesidad_hospital()
        return
    
    abrir_via_aerea()
    
    if respira():
        permitir_posicion_ventilacion()
        return
    
    administrar_ventilaciones()
    
    while True:
        if signos_de_vida():
            reevaluar_espera_ambulancia()
        elif llego_ambulancia():
            print("Fin del procedimiento. La ambulancia ha llegado.")
            break
        else:
            administrar_compresiones()

def responde_a_estimulos():
    return obtener_respuesta_si_no("¿Responde a estímulos?")

def valorar_necesidad_hospital():
    print("Valorar la necesidad de llevarlo al hospital más cercano.")

def abrir_via_aerea():
    print("Abriendo la vía aérea...")

def respira():
    return obtener_respuesta_si_no("¿Respira?")

def permitir_posicion_ventilacion():
    print("Permitirle posición de suficiente ventilación.")

def administrar_ventilaciones():
    print("Administrando 5 ventilaciones y llamando a la ambulancia...")

def signos_de_vida():
    return obtener_respuesta_si_no("¿Hay signos de vida?")

def llego_ambulancia():
    return obtener_respuesta_si_no("¿Llegó la ambulancia?")

def reevaluar_espera_ambulancia():
    print("Reevaluando a la espera de la ambulancia...")

def administrar_compresiones():
    print("Administrando compresiones torácicas hasta que llegue la ambulancia...")

if __name__ == "__main__":
    primeros_auxilios()