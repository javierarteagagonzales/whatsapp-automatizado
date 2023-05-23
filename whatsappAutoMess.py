import pywhatkit

numTel = str(input("Por favor digite su número"))
mensaje = str(input("Introduzca el mensaje"))
horas = int(input("Por favor digite la hora"))
minutos = int(input("Por favor digite los minutos"))

pywhatkit.sendwhatmsg ("51"+numTel,mensaje, horas, minutos, 4, True, 4)