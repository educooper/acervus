# utils/whatsapp.py
import pywhatkit as kit
from datetime import datetime, timedelta

def send_whatsapp_message(phone_number, message):
    now = datetime.now() + timedelta(minutes=2)  # espera 2 minutos
    hour = now.hour
    minute = now.minute

    try:
        kit.sendwhatmsg(phone_number, message, hour, minute)
        return True
    except Exception as e:
        print(f"Erro ao enviar WhatsApp: {e}")
        return False
