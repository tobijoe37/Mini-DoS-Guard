
from blocker import block_ip

print("===== WINDOWS FIREWALL TEST =====")

test_ip = "198.51.100.25"

result = block_ip(test_ip)

if result:
    print("[SUCCESS] Firewall rule creation confirmed.")
else:
    print("[FAILED] Firewall rule was not created.")
