import os
import requests
from dotenv import load_dotenv

load_dotenv()

def consult_ip(ip):
    chave = os.getenv("ABUSEIPDB_API_KEY")

    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Key": chave,
        "Accept": "application/json"
    }

    parametros = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    resposta = requests.get(
        url,
        headers=headers,
        params=parametros,
        timeout=10
    )
    resposta.raise_for_status()
    
    return resposta        

