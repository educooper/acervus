# utils/whatsapp.py
import pywhatkit as kit
from datetime import datetime, timedelta

#def send_whatsapp_message(phone_number, message):
#    now = datetime.now() + timedelta(minutes=2)  # espera 2 minutos
#    hour = now.hour
#    minute = now.minute


#        kit.sendwhatmsg(phone_number, message, hour, minute)

import pywhatkit as kit
import time

def enviar_codigo_por_whatsapp(telefone, codigo):
    hora = time.localtime().tm_hour
    minuto = time.localtime().tm_min + 1  # Aguarda 1 min
    mensagem = f"Seu código de recuperação de senha é: {codigo}"
    try:
        kit.sendwhatmsg(f"+55{telefone}", mensagem, hora, minuto)
        return True
    except Exception as e:
        print(f"Erro ao enviar WhatsApp: {e}")
        return False
