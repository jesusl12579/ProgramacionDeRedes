#Actividad de Laboratorio 
#Nombre: Jose de Jesus Lucio Tovar 
#Fecha: 19-septiembre-2024


hour = int (input("Hora de inicio(horas): "))
mins = int (input("Minuto de inicio(minutos): "))
dura = int (input("Duracion del evento (minutos): "))

total = mins + dura
cociente = total // 60
residuo = total % 60
hour += cociente

print(str (hour) + ':' + str(residuo))

