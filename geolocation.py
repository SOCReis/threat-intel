import requests


def get_ip_info(ip):
    url = f"https://ipwho.is/{ip}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    if not data.get("success"):
        raise ValueError("Não foi possível consultar esse IP.")

    return data