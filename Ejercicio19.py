respuestas_correctas = int(input("numero de respuestas correctas: "))
respuestas_incorrectas = int(input("numero de respuestas incorrectas: "))
respuestas_en_blanco = int(input("numero de respuestas en blanco: "))

PUNTOS_CORRECTA = respuestas_correctas * 5
PUNTOS_INCORRECTA = respuestas_incorrectas *-1
PUNTOS_BLANCO = respuestas_en_blanco * 0

NotaFinal = PUNTOS_CORRECTA + PUNTOS_INCORRECTA + PUNTOS_BLANCO
print(f'Tu nota final es: {NotaFinal}')
