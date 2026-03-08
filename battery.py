import psutil

def battery():
    battery = psutil.sensors_battery()
    percentual = battery.percent
    loading = battery.power_plugged
    secs = battery.secsleft

    print(f"\n--- Status da Bateria ---")
    print(f"Carga atual: {percentual}%")
    print(f"Status: {'Carregando ⚡' if loading else 'Descarregando 🔋'}")

    if not loading:
        if secs == psutil.POWER_TIME_UNKNOWN:
            print("Tempo restante: Calculando...")
        else:
            horas = secs // 3600
            minutos = (secs % 3600) // 60
            print(f"Tempo restante: {horas}h {minutos}min")
    else:
        print("Conectado à fonte de energia.")
    print("-" * 25)

if __name__ == "__main__":
    battery()