
H_partida = int(input("Hora de partida (HH): "))
M_partida = int(input("Minutos de partida (MM): "))
S_partida = int(input("Segundos de partida (SS): "))
TiempoT = int(input("Tiempo de viaje total en segundos (T): "))

segundosT = (H_partida * 3600) + (M_partida * 60) + S_partida

segundos_llegada_total = segundos_T + TiempoT


H_llegada = (segundos_llegada_total // 3600) % 24

M_llegada = (segundos_llegada_total % 3600) // 60

S_llegada = segundos_llegada_total % 60

print(f"Hora de llegada: {HH_llegada:02}:{MM_llegada:02}:{SS_llegada:02}")
