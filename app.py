import pywhatkit as pwk
import time

# Código de país
codigo_pais = "+57"

# Lee los números de teléfono desde un archivo
with open('numeros.txt', 'r') as file:
    numbers = file.readlines()

# Mensaje que quieres enviar
mensaje = "Hola, buenos días. Estoy interesado en obtener información sobre las opciones de financiamiento para un posgrado virtual en la CUC. Me gustaría saber que opciones ofrecen, cuáles son las tasas, los plazos y los requisitos para aplicar. El valor sería de $10.300.000. Muchas gracias."

# Tiempo entre mensajes (en segundos)
delay = 10

for number in numbers:
    # Elimina espacios en blanco y saltos de línea
    number = number.strip()
    
    # Añade el código de país si no está presente
    if not number.startswith("+"):
        number = codigo_pais + number
    
    # Enviar el mensaje
    try:
        pwk.sendwhatmsg_instantly(number, mensaje, 12, True, 5)
        print(f"Mensaje enviado a {number}")
        
        # Esperar un tiempo para evitar ser bloqueado por WhatsApp
        print(f"Esperando {delay} segundos...")
        #time.sleep(delay)
    except Exception as e:
        print(f"No se pudo enviar el mensaje a {number}. Error: {e}")
