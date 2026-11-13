
from collections import defaultdict, deque
from logger import log_event
from blocker import block_ip

THRESHOLD = 5
TIME_WINDOW = 10

ip_requests = defaultdict(deque)
flagged_ips = set()
blocked_ips = set()


def detect_dos(ip_address, current_time):

    if ip_address in flagged_ips:
        return

    requests = ip_requests[ip_address]

    while requests and current_time - requests[0] > TIME_WINDOW:
        requests.popleft()

    requests.append(current_time)

    print(f"Request received from: {ip_address}")

    if len(requests) >= THRESHOLD:

        flagged_ips.add(ip_address)

        print("\n[ALERT] Suspicious traffic detected!")
        print(f"[ALERT] IP Address: {ip_address}")

        log_event(f"Suspicious traffic detected from {ip_address}")

        print("[ACTION] Attempting Windows Firewall block...")

        if block_ip(ip_address):
            blocked_ips.add(ip_address)
            log_event(f"Windows Firewall successfully blocked {ip_address}")
        else:
            print("[FAILED] Firewall did not block this IP.")
            log_event(f"Firewall failed to block {ip_address}")


traffic = [
    ("198.51.100.25", 1),
    ("203.0.113.20", 2),
    ("198.51.100.25", 3),
    ("198.51.100.25", 4),
    ("198.51.100.25", 5),
    ("198.51.100.25", 6),
    ("198.51.100.25", 7),
]

print("===== MINI DOS GUARD =====\n")

for ip, timestamp in traffic:
    detect_dos(ip, timestamp)

print("\n===== SUCCESSFULLY BLOCKED IP ADDRESSES =====")

for ip in blocked_ips:
    print(ip)

print("\n===== SCAN COMPLETE =====")
