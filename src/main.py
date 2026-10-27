import requests
from validator.validator import validate_ip_address
from intelligence.geolocation import get_ip_info
from reports.report import report_results
from intelligence.abuseipdb import consult_ip

input_ip = input("Enter an IP: ").strip()

if validate_ip_address(input_ip):
    print(f"\nIP valid: {input_ip}")

    try:
        abuse_response = consult_ip(input_ip)
        abuse_data = abuse_response.json()["data"]
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
            "Abuse Score": abuse_data.get("abuseConfidenceScore"),
            "Total Reports": abuse_data.get("totalReports"),
            "Last Reported At": abuse_data.get("lastReportedAt"),
        })
        

    except (ValueError, requests.RequestException) as e:
        print(f"Query error: {e}")

else:
    print(f"{input_ip} not a valid IP.")