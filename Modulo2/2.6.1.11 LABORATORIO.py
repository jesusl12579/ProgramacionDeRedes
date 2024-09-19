# Función para calcular el tiempo final
def calcular_tiempo_final(hora_inicio, minuto_inicio, duracion_minutos):
    # Sumar los minutos de la duración a los minutos de inicio
    minuto_final = minuto_inicio + duracion_minutos
    
    # Calcular las horas adicionales si los minutos exceden 59
    horas_adicionales = minuto_final // 60
    minuto_final = minuto_final % 60
    
    # Sumar las horas adicionales a la hora de inicio
    hora_final = hora_inicio + horas_adicionales
    
    # Asegurar que la hora final esté en formato de 24 horas
    hora_final = hora_final % 24
    
    return hora_final, minuto_final

# Entradas
hora = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Calcular el tiempo final
hora_final, minuto_final = calcular_tiempo_final(hora, mins, dura)

# Mostrar el resultado
print(f"El evento termina a las {hora_final:02d}:{minuto_final:02d}")


