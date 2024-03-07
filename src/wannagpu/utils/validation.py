import regex


def is_valid_ip(ip_address: str):
    pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    if regex.match(pattern, ip_address):
        return True
    else:
        return False

