import pyautogui, webbrowser
from time import sleep

# Segundos que espera el programa para escribir los mensajes. ¡Dejar tiempo para abirir el navegador en la pestaña!
segundos = 60

# Menu
print("\n====================")
print("Programa para enviar mensajes de Whatsapp.")
print("Create By: Dajachi")
print("\n¡Importante!")
print("No excederse con el número de\nmensajes si tienes un PC de bajos recursos.")
print("\nAntes de enviar el mensaje, tienes que iniciar sessión en\nWhatsapp Web.")
print("\n\nUltima actualización: 4/01/2025")
print("====================")

# Variables
numero = input("\nDigite el número de telefono con la extención (Ejemplo: +57000000000): ")
veces = int(input("\nNúmero de mensajes a enviar: "))
mensaje = input("\n¿Cual es el mensaje?: ")

# Abrir el navegador predeterminado en la url del chat
webbrowser.open(f'https://web.whatsapp.com/send?phone={numero}')

print("\nAbriendo el navegador...")
print(f"Esperando {segundos} segundos para enviar el mensaje...")
print("¡No interrumpa la ejecución del programa!")

# Esperar los segundos para escribir los mensajes
sleep(segundos)

# Bucle para escribir y enviar los mensajes
for i in range(veces):
    pyautogui.write(mensaje)
    pyautogui.press('enter')
