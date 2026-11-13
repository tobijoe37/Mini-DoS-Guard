
import ipaddress
import subprocess

def block_ip(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)
    except ValueError:
        print("[ERROR] Invalid IP address")
        return False

    if ip.is_loopback or ip.is_link_local:
        print(f"[WARNING] Cannot block local IP: {ip}")
        return False

    rule_name = f"MiniDoSGuard_{ip}"

    command = [
        "netsh", "advfirewall", "firewall", "add", "rule",
        f"name={rule_name}",
        "dir=in",
        "action=block",
        f"remoteip={ip}",
        "enable=yes",
        "profile=any"
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"[SUCCESS] Windows Firewall blocked {ip}")
            return True

        print("[ERROR] Firewall blocking failed")
        print(result.stderr or result.stdout)
        return False

    except Exception as error:
        print(f"[ERROR] {error}")
        return False
