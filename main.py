import requests
from validator import validate_ip_address
from geolocation import get_ip_info
from report import report_results

input_ip = input("Enter an IP: ").strip()

if validate_ip_address(input_ip):
    print(f"\nIP valid: {input_ip}")

    try:
        ip_info = get_ip_info(input_ip)

        connection = ip_info.get("connection") or {}
        report_results(input_ip, True, {
            "IP": ip_info.get("ip"),
            "Type": ip_info.get("type"),
            "Continent": ip_info.get("continent"),
            "Country": ip_info.get("country"),
            "Region": ip_info.get("region"),
            "City": ip_info.get("city"),
            "Latitude": ip_info.get("latitude"),
            "Longitude": ip_info.get("longitude"),
            "ISP": connection.get("isp"),
            "Organization": connection.get("org"),
        })
        

    except (ValueError, requests.RequestException) as e:
        print(f"Query error: {e}")

else:
    print(f"{input_ip} not a valid IP.")