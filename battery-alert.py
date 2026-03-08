import psutil
import tkinter as tk
from tkinter import messagebox
import time
from datetime import datetime

lowBatteryLimit = 20
checkDelay = 60 # verificação em segundos
LogFileName = "battery_history.txt"

def saveBatteryLog(currentPercent, status):
    # Função para salvar o histórico em um arquivo de texto
    currentTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(LogFileName, "a", encoding="utf-8") as logFile:
        logFile.write(f"[{currentTime}] Percent: {currentPercent}% | Status: {status}\n")

def triggerAlert(currentPercent):
    # Função para exibir a janela de aviso visual
    alertRoot = tk.Tk()
    alertRoot.withdraw()
    messagebox.showwarning(
        "Low Battery Warning ⚠️", 
        f"Your battery is at {currentPercent}%. Please connect your charger! ⚠️"
    )
    alertRoot.destroy()

print("🚀 Battery Monitor with Logging active...")

while True:
    batteryData = psutil.sensors_battery()
    batteryPercent = batteryData.percent
    isPowerPlugged = batteryData.power_plugged
    
    powerStatus = "Charging ⚡" if isPowerPlugged else "Discharging 🔋"

    saveBatteryLog(batteryPercent, powerStatus)
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {batteryPercent}% | {powerStatus}")

    if batteryPercent <= lowBatteryLimit and not isPowerPlugged:
        saveBatteryLog(batteryPercent, "🚨 ALERT TRIGGERED - CRITICAL LEVEL")
        triggerAlert(batteryPercent)
        time.sleep(300) 
    
    time.sleep(checkDelay)