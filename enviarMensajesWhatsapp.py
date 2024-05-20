import pyautogui, webbrowser
from time import sleep

# Menu
print("\n====================")
print("Programa para enviar mensajes de Whatsapp.")
print("Create By: Dajachi")
print("\n¡Importante!")
print("No excederse con el número de\nmensajes si tienes un PC de bajos recursos.")
print("\nAntes de enviar el mensaje, tienes que iniciar sessión en\nWhatsapp Web.")
print("====================")

numero = input("\nDigite el número de telefono con la extención (Ejemplo: +57000000000): ")
veces = int(input("\nNúmero de mensajes a enviar: "))
mensaje = input("\n¿Cual es el mensaje?: ")

webbrowser.open(f'https://web.whatsapp.com/send?phone={numero}')

print("\nAbriendo el navegador...")
print("Esperando 70 segundos para enviar el mensaje...")
print("¡No interrumpa la ejecución del programa!")

sleep(70)

for i in range(veces):
    pyautogui.write(mensaje)
    pyautogui.press('enter')
