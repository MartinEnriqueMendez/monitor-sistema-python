import os
from dotenv import load_dotenv
import psutil
import requests
import time

# Se cargan las variables del .env
load_dotenv()

# --- Configuracion ---
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
UMBRAL_CPU = 90.0
UMBRAL_RAM = 90.0
URL_API_PRECIOS = "http://127.0.0.1:8000/productos" #Url verifica productos de proyecto anterior, entra a fondo y confirma que el JSON de productos está listo para ser servido

def enviar_alerta(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": f" ALERTA DE SISTEMA \n\n{mensaje}"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error enviando Telegram: {e}")
    
def verificar_api():
    """Intente conectar con la API de precios para ver si está online """
    try:
        response = requests.get(URL_API_PRECIOS, timeout = 5)
        if response.status_code != 200:
            return False
        return True
    except:
        return False
    
print("MonitorSys_Bot iniciando... vigilando servidor.")
    
while True:
    # 1. Monitorear Hardware
    uso_cpu = psutil.cpu_percent(interval = 1)
    uso_ram = psutil.virtual_memory().percent
    
    # 2. Monitorear servicio (API)
    api_online = verificar_api()
    
    # Lógica de alertas
    if uso_cpu > UMBRAL_CPU:
        enviar_alerta(f"CPU al límite: {uso_cpu}%")
        
    if uso_ram > UMBRAL_RAM:
        enviar_alerta(f"Memoria RAM crítica: {uso_ram}%")
    
    if not api_online:
        enviar_alerta("¡LA API DE PRECIOS SE HA CAÍDO!")
        
    #Esperar 60 segundos antes del próximo chequeo (para no saturar)
    time.sleep(60)