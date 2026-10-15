def report_results(ip_address, is_valid, ip_info=None):
    print(f"IP Address: {ip_address}")
    print(f"Valid: {is_valid}")

    if is_valid and ip_info:
        print("IP Information:")
        for key, value in ip_info.items():
            print(f"{key}: {value}")
